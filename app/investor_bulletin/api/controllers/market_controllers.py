from typing import Optional

from fastapi import APIRouter, Query

from resources.market.market_schema import StockResponse, Symbol
from resources.market.market_service import get_market_data


router = APIRouter()


@router.get("")
async def get_market_data_route(
    symbol: Optional[Symbol] = Query(
        None, title="Symbol", description="The symbol of the stock", example="AAPL"
    )
) -> StockResponse:
    """
    _summary_
    this function to get the latest market prices for mentioned symbols.

    __parameters__
    - symbol: The symbol of the stock. (optional)

    __response__
    - StockResponse: The response containing the stock data for the sent symbols in the request.
    """
    symbol_param = (
        f"{Symbol.AAPL},{Symbol.MSFT},{Symbol.GOOG},{Symbol.AMZN},{Symbol.META}"
    )
    if symbol:
        symbol_param = symbol.value
    print(f"Getting market data for {symbol_param}")
    return await get_market_data(symbol=symbol_param)
