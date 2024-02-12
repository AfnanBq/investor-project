""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
from resources.alerts.alert_dal import create_alert, get_alerts
from resources.alerts.alert_schema import AlertCreate


def create_new_alert(rule: AlertCreate, session):
    """ "Helper function to create a new alert.
    Args:
    - rule: AlertCreate - The alert to create containing the alert rule ID.
    - session: Session - The database session.
    Returns:
    - Alert - The created alert.
    """
    create_alert(rule=rule, session=session)


def get_all_alerts(session):
    """Helper function to get all alerts.
    Args:
    - session: Session - The database session.
    Returns:
    - AlertList - A list of all alerts.
    """
    return get_alerts(session=session)
