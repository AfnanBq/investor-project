""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from typing import Dict, List
from uuid import UUID

from db.models.models import AlertRule
from resources.alert_rules.alert_rule_schema import AlertRuleCreate,AlertRuleUpdate
from sqlalchemy.exc import DBAPIError,SQLAlchemyError
from sqlalchemy.orm import Session


def create_alert_rule (rule: AlertRuleCreate,session: Session) -> None:
    """Create an alert rule."""
    try:
        new_rule = AlertRule(
            name = rule.name,threshold_price = rule.threshold_price,symbol = rule.symbol
        )
        session.add(new_rule)
        session.commit()
    except (SQLAlchemyError,DBAPIError) as error:
        session.rollback()
        print(f"Database error: {error}")
        raise error


def get_rule_by_id (rule_id: UUID,session: Session) -> AlertRule:
    """Get an alert rule by ID."""
    try:
        return (
            session.query(AlertRule).filter(AlertRule.alert_rule_id == rule_id).first()
        )
    except (SQLAlchemyError,DBAPIError) as error:
        print(f"Database error: {error}")
        raise error


def get_alert_rules (session: Session) -> List[AlertRule]:
    """Get all alert rules."""
    try:
        return session.query(AlertRule).all()
    except (SQLAlchemyError,DBAPIError) as error:
        print(f"Database error: {error}")
        raise error


def update_rule (rule_id: UUID,rule: AlertRuleUpdate,session: Session) -> None:
    """Update an alert rule by ID."""
    try:
        session.query(AlertRule).filter(AlertRule.alert_rule_id == rule_id).update(rule)
        session.commit()
    except (SQLAlchemyError,DBAPIError) as error:
        session.rollback()
        print(f"Database error: {error}")
        raise error


def delete_rule (rule_id: UUID,session: Session) -> None:
    """Delete an alert rule by ID."""
    try:
        session.query(AlertRule).filter(AlertRule.alert_rule_id == rule_id).delete()
        session.commit()
    except (SQLAlchemyError,DBAPIError) as error:
        session.rollback()
        print(f"Database error: {error}")
        raise error

def get_alert_rule_ids_crossed_threshold(session: Session, market_data: Dict[str, float]) -> List[UUID]:
    """Get all alert rule ids that have crossed the threshold."""
    try:
        rules = session.query(AlertRule).filter(AlertRule.symbol.in_(list(market_data.keys()))).all()
        alert_rule_ids = []

        for rule in rules:
            print(f"Checking rule {rule.alert_rule_id}...")
            if float(rule.threshold_price) == market_data[rule.symbol]:
                print(f"Rule {rule.alert_rule_id} has crossed the threshold.")
                alert_rule_ids.append(rule.alert_rule_id)
        return alert_rule_ids
    except (SQLAlchemyError,DBAPIError) as error:
        print(f"Database error: {error}")
        raise error
