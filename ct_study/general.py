from lib import Log
from config import config
import pika, json
from orthanc_export import orthanc_export
from mysql_module import insert_row

def callback(ch, method, properties, body):
    try:
        insert_row(orthanc_export(json.loads(body)))
        Log().info("Orthanc export success")
    except:
        Log().error("Orthanc export error", exc_info=True)

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(config.RABBIT_HOST))
    Log().info("Connection to Rabbit Success")
except:
    Log().error("Connection to Rabbit Failed", exc_info=True)
channel = connection.channel()
channel.queue_declare(queue = 'ct_queue', durable = True)
channel.basic_consume(queue = 'ct_queue', on_message_callback = callback, auto_ack = True)
channel.start_consuming()
Log().info("Consuming started")