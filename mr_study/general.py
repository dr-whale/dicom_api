from lib import Log
from config import config
import pika, json

def callback(ch, method, properties, body):
    print('Callback')
    Log().info(json.loads(body))

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(config.RABBIT_HOST))
    Log().info("Connection to Rabbit Success")
except:
    Log().error("Connection to Rabbit Failed", exc_info=True)
channel = connection.channel()
channel.queue_declare(queue = 'mr_queue', durable = True)
channel.basic_consume(queue = 'mr_queue', on_message_callback = callback, auto_ack = True)
channel.start_consuming()
Log().info("Consuming started")