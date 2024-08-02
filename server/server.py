import pika
import json
from datetime import datetime
import pymongo
import logging
# MongoDB settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "mqtt_db"
COLLECTION_NAME = "messages"

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# RabbitMQ settings
RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'mqtt_queue'

# Connect to RabbitMQ
try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    print("Connected to RabbitMQ")
except Exception as e:
    print(f"Failed to connect to RabbitMQ: {e}")
    exit(1)

# Connect to RabbitMQ
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
# channel = connection.channel()

# Declare the queue
channel.queue_declare(queue=QUEUE_NAME, durable=True)
print(f"Declared queue {QUEUE_NAME}")


# Callback function to handle messages
def callback(ch, method, properties, body):
    # import pdb;pdb.set_trace()
    try:
        
        print("Received a message")
        # message = json.loads(body)
        message_str = body.decode('utf-8')
        print(f"Raw message: {message_str}")

        message = json.loads(message_str)
        logger.debug(f"Received message: {message}")

        # message = json.loads(body.decode('utf-8'))
        # print("message1", message)
        message['timestamp'] = datetime.now()
        result = collection.insert_one(message)
        logger.debug(f"Stored message with id: {result.inserted_id}")
        print(message['timestamp'])
        print(f"Stored message with id: {result.inserted_id}")
        print("Hello")
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

# Set up the consumer
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
print("Consumer set up complete")

print('start consuming.......')
channel.start_consuming()
