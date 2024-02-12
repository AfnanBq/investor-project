""" Alert Schema """
"""_summary_
This file to abstract any validation logic for the Alerts
"""

from typing import List
from uuid import UUID

from pydantic import BaseModel



class Alert(BaseModel):
    alert_id: UUID
    alert_rule_id: UUID
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True


class AlertCreate(BaseModel):
    alert_rule_id: UUID


class AlertList(BaseModel):
    alerts: List[Alert]
