""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from db.models import Alert
from resources.alerts.alert_schema import AlertCreate
from sqlalchemy.exc import DBAPIError, SQLAlchemyError


def create_alert(alert: AlertCreate, session):
    """Create an alert."""
    try:
        new_alert = Alert(alert_rule_id=alert.alert_rule_id)
        session.add(new_alert)
        session.commit()
    except (SQLAlchemyError, DBAPIError) as error:
        print(error)
        raise error


def get_alerts(session):
    """Get all alerts."""
    try:
        return session.query(Alert).all()
    except (SQLAlchemyError, DBAPIError) as error:
        print(error)
        raise error
