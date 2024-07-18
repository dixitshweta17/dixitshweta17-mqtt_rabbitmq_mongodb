import pika
import json
from datetime import datetime
import pymongo

# MongoDB settings
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
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue=QUEUE_NAME, durable=True)

# Callback function to handle messages
def callback(ch, method, properties, body):
    # import pdb;pdb.set_trace()
    try:
        
        print("Received a message")
        # message = json.loads(body)
        message = json.loads(body.decode('utf-8'))
        print("message1", message)
        message['timestamp'] = datetime.now()
        collection.insert_one(message)
        print("message", message)
        print("Hello")
    except Exception as e:
        print(f"An error occurred: {e}")

# Set up the consumer
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)


print('Hello world')
channel.start_consuming()
