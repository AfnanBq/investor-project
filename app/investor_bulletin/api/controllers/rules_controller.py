from uuid import UUID

from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.models.dependencies import get_db
from resources.alert_rules.alert_rule_schema import (
    AlertRuleCreate,
    AlertRuleUpdate,
    SuccessResponse,
    AlertRuleList,
)
from resources.alert_rules.alert_rule_service import (
    create_new_rule,
    delete_alert_rule,
    get_alert_rule_by_id,
    get_all_rules,
    update_alert_rule,
)
from resources.alerts.alert_schema import AlertList
from resources.alerts.alert_service import get_all_alerts



router = APIRouter()


@router.post("")
def create_rule(
    body: AlertRuleCreate = Body(...), session: Session = Depends(get_db)
) -> SuccessResponse:
    """
    __summary__
    Create a new alert rule.

    __params__
    - body: AlertRuleCreate - The alert rule to create.
    - session: Session - The database session.

    __raises__
    - HTTPException: 500 - If a server error occurs.

    """
    try:
        create_new_rule(rule=body, session=session)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"A server error occurred",
        )
    return {"message": "Alert Rule Created Successfully!"}


@router.patch("/{id}")
def update_rule(
    id: UUID, body: AlertRuleUpdate = Body(...), session: Session = Depends(get_db)
) -> SuccessResponse:
    """
    __summary__
    Update an alert rule.

    __params__
    - id: UUID - The ID of the alert rule to update.
    - body: AlertRuleCreate - The updated alert rule.
    - session: Session - The database session.

    __returns__
    - AlertRule - The updated alert rule.

    __raises__
    - HTTPException: 404 - If the alert rule is not found.
    - HTTPException: 500 - If a server error occurs.
    """
    alert_rule_in_db = get_alert_rule_by_id(rule_id=id, session=session)
    if not alert_rule_in_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Alert Rule {id} not found."
        )
    try:
        rule_update = body.dict(exclude_unset=True)
        update_alert_rule(rule_id=id, rule=rule_update, session=session)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"A server error occurred",
        )
    return {"message": f"Alert Rule {id} Updated Successfully!"}


@router.delete("/{id}")
def delete_rule(id: UUID, session: Session = Depends(get_db)) -> SuccessResponse:
    """
    __summary__
    Delete an alert rule.

    __params__
    - id: UUID - The ID of the alert rule to delete.
    - session: Session - The database session.

    __returns__
    - SuccessResponse - A success message.

    __raises__
    - HTTPException: 404 - If the alert rule is not found.
    """
    alert_rule_in_db = get_alert_rule_by_id(rule_id=id, session=session)
    if not alert_rule_in_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Alert Rule {id} not found."
        )
    try:
        delete_alert_rule(rule_id=id, session=session)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"A server error occurred",
        )
    return {"message": f"Alert Rule {id} Deleted Successfully!"}


@router.get("")
def get_rules(session: Session = Depends(get_db)) -> AlertRuleList:
    """Get all alert rules from the database."""
    try:
        rules = get_all_rules(session=session)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"A server error occurred",
        )
    return AlertRuleList(alert_rules=rules)


@router.get("/alerts")
def get_alerts(session: Session = Depends(get_db)) -> AlertList:
    """Get all alerts from the database."""
    try:
        alerts = AlertList(alerts=get_all_alerts(session=session))
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"A server error occurred",
        )
    return alerts
