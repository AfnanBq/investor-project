""" Alert Rule Model """
from sqlalchemy import Column, DateTime, String, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.model_base import Base


class AlertRule(Base):
    __tablename__ = "alert-rules"
    alert_rule_id = Column(
        UUID, primary_key=True, server_default=func.uuid_generate_v4()
    )
    name = Column(String, nullable=False, unique=True)
    threshold_price = Column(Numeric, nullable=False)
    symbol = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )
    alerts = relationship("Alert", back_populates="alert_rule")
