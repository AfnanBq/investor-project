import json

from pika import BlockingConnection, ConnectionParameters

from resources.alerts.alert_schema import AlertCreate
from resources.alerts.alert_service import create_new_alert
from db.models.model_base import SessionLocal
from resources.config import settings


def init_subscriber():
    return BlockingConnection(ConnectionParameters(host=settings.RABBITMQ_HOST))


def verify_message_validity(message):
    if message is None:
        print(f"Empty event data received")
        return False
    if "event_name" not in message.keys() or "event_data" not in message.keys():
        print(f"Invalid event data received: {message}")
        return False
    return True


def on_event(channel, method, properties, body):
    session = SessionLocal()
    print(f"Received message: {body}")
    data = json.loads(body)
    if not verify_message_validity(data):
        return
    if data["event_name"] == "THRESHOLD_ALERT":
        print(f"Received THRESHOLD_ALERT event...")
        event_data = data["event_data"]
        if "alert_rule_id" not in event_data.keys():
            print(f"No alert rule ID found in {event_data}")
            return
        create_new_alert(alert=AlertCreate(alert_rule_id=event_data["alert_rule_id"]), session=session)


if __name__ == "__main__":
    print("Message broker subscriber is running...")
    subscriber = init_subscriber()
    channel = subscriber.channel()
    channel.queue_declare(queue="alerts", durable=True)
    channel.basic_consume(queue="alerts", on_message_callback=on_event, auto_ack=True)
    print("Waiting for messages...")
    channel.start_consuming() 

    print("Closing connection...")
    subscriber.close()
