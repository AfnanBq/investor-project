""" Alert Model """
from db.models.model_base import Base
from sqlalchemy import Column,DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Alert(Base):
    __tablename__ = "alerts"
    alert_id = Column(UUID,primary_key = True,server_default = func.uuid_generate_v4())
    alert_rule_id = Column(
        UUID,ForeignKey("alert-rules.alert_rule_id"),nullable = False
    )
    alert_rule = relationship("AlertRule",back_populates = "alerts")
    created_at = Column(DateTime,default = func.now(),nullable = False)
    updated_at = Column(
        DateTime,server_default = func.now(),onupdate = func.now(),nullable = False
    )
