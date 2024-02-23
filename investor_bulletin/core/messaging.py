import json
import uuid

from amqpstorm import Connection, Message
from resources.config import settings


def publish(message):
    try:
        broker = Connection(settings.RABBITMQ_HOST, settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
        channel = broker.channel()
        queue_name = 'threshold_alert'
        channel.queue.declare(queue=queue_name, durable=True)

        # Publish a message to the queue
        message_body = {
            "event_name": "THRESHOLD_ALERT",
            "event_data": message,
        }

        msg = Message.create(channel, body=json.dumps(message_body))
        msg.publish(routing_key='threshold_alert')
        print(f"Sent '{message_body}' to {queue_name} queue successfully!")

    finally:
        broker.close()


if __name__ == '__main__':
    # Call the send_message function with the desired message
    alert_rule_id = str(uuid.uuid4())
    message = {"alert_rule_id": alert_rule_id}
    publish(message)
