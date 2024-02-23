""" Market Schema """
"""_summary_
This file to abstract any validation logic for the Market
"""

from enum import Enum
from typing import Any,Dict

from pydantic import BaseModel,Field


class TwelveDataEndpoints(str,Enum):
    """Twelve Data Endpoints"""

    RealTimePrice = "price"


class Symbol(str,Enum):
    """Symbol"""

    AAPL = "AAPL"
    MSFT = "MSFT"
    GOOG = "GOOG"
    AMZN = "AMZN"
    META = "META"


class StockResponse(BaseModel):
    """Market Response"""

    stocks: Dict[str,Any] = Field(
        ...,title = "Stocks",description = "The stocks and their prices"
    )
