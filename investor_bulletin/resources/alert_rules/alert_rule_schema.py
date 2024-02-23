""" Alert Rule Schema """
"""_summary_
This file to abstract any validation logic for the Alert Rules
"""

from datetime import datetime
from typing import List,Optional
from uuid import UUID

from pydantic import BaseModel,PositiveFloat,Field
from resources.market.market_schema import Symbol


class AlertRule(BaseModel):
    alert_rule_id: UUID
    name: str
    threshold_price: PositiveFloat
    symbol: Symbol
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AlertRuleCreate(BaseModel):
    name: str = Field(
        ...,
        title = "Name",
        description = "The name of the alert rule",
        example = "Alert Rule 1",
    )
    threshold_price: PositiveFloat = Field(
        ...,
        title = "Threshold Price",
        description = "The threshold price for the alert rule",
        example = 100.0,
    )
    symbol: Symbol = Field(
        ...,
        title = "Symbol",
        description = "The symbol that design the rule for",
        example = "AAPL",
    )


class AlertRuleUpdate(BaseModel):
    name: Optional[str] = Field(
        None,
        title = "Name",
        description = "The name of the alert rule",
        example = "Alert Rule 1",
    )
    threshold_price: Optional[PositiveFloat] = Field(
        None,
        title = "Threshold Price",
        description = "The threshold price for the alert rule",
        example = 100.0,
    )
    symbol: Optional[Symbol] = Field(
        None,
        title = "Symbol",
        description = "The symbol that design the rule for",
        example = "AAPL",
    )


class AlertRuleList(BaseModel):
    alert_rules: List[AlertRule]


class SuccessResponse(BaseModel):
    message: str
