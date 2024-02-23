# Description: This file contains the Celery tasks that will be executed by the Celery worker.

import json
from resources.market.market_service import get_market_data
from resources.market.market_schema import Symbol
from resources.alert_rules.alert_rule_service import get_crossed_threshold_ids
from db.models.model_base import SessionLocal
from core.messaging import publish
from celery.schedules import crontab
from worker.app import app
from asgiref.sync import async_to_sync

# schedule the task to run every 5 minutes
app.conf.beat_schedule = {
    "fetch-market-data-every-5-minutes": {
        "task": "worker.tasks.fetch_market_data",
        "schedule": crontab(minute="*/5"),
    },
}

@app.task
def fetch_market_data():
    print("Fetching market data...")
    # get the latest market data for the symbols
    symbols = (
        f"{Symbol.AAPL.value},{Symbol.MSFT.value},{Symbol.GOOG.value},{Symbol.AMZN.value},{Symbol.META.value}"
    )
    market_data = async_to_sync(get_market_data)(symbol = symbols)
    # convert the market data to a dictionary where the key is the symbol and the value is the price
    market_data = market_data["stocks"]
    market_data = {symbol: round(float(data["price"]),2) for symbol, data in market_data.items()}

    # get all rules from the database
    session = SessionLocal()
    alert_rules_ids = get_crossed_threshold_ids(session=session, market_data=market_data)
    session.close()
    print(f"Alert rules that have crossed the threshold: {alert_rules_ids}")
    for rule_id in alert_rules_ids:
        print(f"Publishing alert for rule ID: {rule_id}")
        message = {"alert_rule_id": str(rule_id)}
        publish(message=message, queue_name="alerts", routing_key="alerts", event_name="THRESHOLD_ALERT")
