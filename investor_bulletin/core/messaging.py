import json
import uuid

from amqpstorm import Connection, Message
from resources.config import settings


def publish(message, queue_name, routing_key, event_name):
    try:
        broker = Connection(settings.RABBITMQ_HOST, settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
        channel = broker.channel()
        queue_name = queue_name
        channel.queue.declare(queue=queue_name, durable=True)

        # Publish a message to the queue
        message_body = {
            "event_name": event_name,
            "event_data": message,
        }

        msg = Message.create(channel, body=json.dumps(message_body))
        msg.publish(routing_key=routing_key)
        print(f"Sent '{message_body}' to {queue_name} queue successfully!")

    finally:
        broker.close()
