""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
from uuid import UUID

from resources.alert_rules.alert_rule_dal import (
    create_alert_rule,
    delete_rule,
    get_rule_by_id,
    get_alert_rules,
    update_rule,
)
from resources.alert_rules.alert_rule_schema import AlertRuleCreate,AlertRuleUpdate, AlertRule, AlertRuleList


def create_new_rule (rule: AlertRuleCreate,session) -> None:
    """ "Helper function to create a new alert rule.
    Args:
    - rule: AlertRuleCrudBase - The alert rule to create containing the name, threshold price, and symbol.
    - session: Session - The database session.
    Returns:
    - AlertRule - The created alert rule.
    """
    create_alert_rule(rule = rule,session = session)


def get_alert_rule_by_id (rule_id: UUID,session) -> AlertRule:
    """Helper function to get an alert rule by ID.
    Args:
    - rule_id: uuid - The ID of the alert rule to get.
    - session: Session - The database session.
    Returns:
    - AlertRule - The alert rule with the given ID.
    """

    return get_rule_by_id(rule_id = rule_id,session = session)


def get_all_rules (session) -> AlertRuleList:
    """Helper function to get all alert rules.
    Args:
    - session: Session - The database session.
    Returns:
    - AlertRuleList - A list of all alert rules.
    """
    return get_alert_rules(session = session)


def update_alert_rule (rule_id: UUID,rule: AlertRuleUpdate,session) -> None:
    """Helper function to update an alert rule.
    Args:
    - rule_id: uuid - The ID of the alert rule to update.
    - rule: AlertRuleCrudBase - The updated alert rule.
    - session: Session - The database session.
    Returns:
    - AlertRule - The updated alert rule.
    """
    update_rule(rule_id = rule_id,rule = rule,session = session)


def delete_alert_rule (rule_id: UUID,session) -> None:
    """Helper function to delete an alert rule.
    Args:
    - rule_id: uuid - The ID of the alert rule to delete.
    - session: Session - The database session.
    """
    delete_rule(rule_id = rule_id,session = session)
