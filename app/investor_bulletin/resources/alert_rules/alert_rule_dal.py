""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from uuid import UUID
from sqlalchemy.exc import DBAPIError, SQLAlchemyError
from sqlalchemy.orm import Session

from db.models import AlertRule
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate


def create_alert_rule(rule: AlertRuleCreate, session: Session):
    """Create an alert rule."""
    try:
        new_rule = AlertRule(
            name=rule.name, threshold_price=rule.threshold_price, symbol=rule.symbol
        )
        session.add(new_rule)
        session.commit()
    except (SQLAlchemyError, DBAPIError) as error:
        session.rollback()
        print(f"Database error: {error}")
        raise error


def get_rule_by_id(rule_id: UUID, session: Session):
    """Get an alert rule by ID."""
    try:
        return (
            session.query(AlertRule).filter(AlertRule.alert_rule_id == rule_id).first()
        )
    except (SQLAlchemyError, DBAPIError) as error:
        print(f"Database error: {error}")
        raise error


def get_alert_rules(session: Session):
    """Get all alert rules."""
    try:
        return session.query(AlertRule).all()
    except (SQLAlchemyError, DBAPIError) as error:
        print(f"Database error: {error}")
        raise error


def update_rule(rule_id: UUID, rule: AlertRuleUpdate, session: Session):
    """Update an alert rule by ID."""
    try:
        session.query(AlertRule).filter(AlertRule.alert_rule_id == rule_id).update(rule)
        session.commit()
    except (SQLAlchemyError, DBAPIError) as error:
        session.rollback()
        print(f"Database error: {error}")
        raise error


def delete_rule(rule_id: UUID, session: Session):
    """Delete an alert rule by ID."""
    try:
        session.query(AlertRule).filter(AlertRule.alert_rule_id == rule_id).delete()
        session.commit()
    except (SQLAlchemyError, DBAPIError) as error:
        session.rollback()
        print(f"Database error: {error}")
        raise error
