""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""
from typing import Dict
from json import JSONDecodeError
from fastapi import HTTPException, status
from httpx import AsyncClient, Response, HTTPError

from resources.config import settings
from resources.market.market_schema import TwelveDataEndpoints


async def request(
    url: str,
    path: str,
    method: str = "GET",
    headers: dict = None,
    params: dict = None,
    timeout: int = None,
) -> Response:
    """
    This function to call external api and return the response

    Args:
    url: str -> the url of the external api
    path: str -> the path of the endpoint
    method: str -> the method of the request
    headers: dict -> the headers of the request
    params: dict -> the params of the request
    timeout: int -> the timeout of the request

    Returns:
    Response -> the response of the request

    Raises:
    - HTTPException with status code 503 if HTTPError occurred while connecting to the external api.
    - HTTPException with status code 500 if JSONDecodeError occurred while decoding the response from the external api.
    - HTTPException with status code 500 if any other error occurred while connecting to the external api.
    """

    async with AsyncClient(
        timeout=timeout,
        http2=True,
    ) as client:
        try:
            print(f"Requesting {method} {url}{path} with with params: {params}")
            response = await client.request(
                method=method,
                url=f"{url}{path}",
                params=params,
                headers=headers,
            )
            response_json = response.json()
            print(f"Response from {url}{path}: {response_json}")
            if response.status_code != status.HTTP_200_OK:
                print(
                    f"The response from {url}{path} is {response_json} with status code: {response.status_code}"
                )
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"{response_json.get('message') or response_json.get('error') or response_json}",
                )

            return response_json
        except HTTPError as error:
            print(f"Error occurred while connecting to {url}{path}.Error: {error}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Something went wrong while retrieving the data. Please try again later.",
            )
        except JSONDecodeError as error:
            print(
                f"Error occurred while decoding the response from {url}{path}.Error: {error}"
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Something went wrong while retrieving the data. Please try again later.",
            )
        except Exception as error:
            print(f"Error occurred while connecting to {url}{path}.Error: {error}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Something went wrong while retrieving the data. Please try again later.",
            )


async def get_market_data(symbol: str) -> Dict[str, Dict]:
    """
    This function to get the market data for the given symbol

    Args:
    symbol: str -> the symbol of the stock

    Returns:
    Dict -> the response containing the price of the stock

    Raises:
    - HTTPException with status code 400 if any error occurred while getting the market data.
    """

    response = await request(
        url=settings.TWELVE_DATA_BASE_URL,
        path=f"{TwelveDataEndpoints.RealTimePrice}",
        headers={
            "X-RapidAPI-Key": settings.RapidAPI_Key,
            "X-RapidAPI-Host": settings.RapidAPI_Host,
        },
        params={"symbol": symbol, "format": "json"},
        timeout=settings.TWELVE_DATA_API_TIMEOUT,
    )
    if response.get("code") and response.get("code") != status.HTTP_200_OK:
        print(
            f"Error occurred while getting the market data. Error: {response.get('message')}"
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{response.get('message')}",
        )
    print(f"Response from get_market_data: {response}")
    return {"stocks": response}
