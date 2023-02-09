import pika, json
from .class_description import Singleton
from config import config
from lib import Log

class Rabbit (metaclass=Singleton):
    def __init__(self):
        self.connection:pika.BlockingConnection = None
        pass

    def check_connection(self):
        if self.connection == None:
            return False
        try:
            self.connection.process_data_events()
        except:
            return False
        return True

    def connect(self):
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(config.RABBIT_HOST))
            self.channel = self.connection.channel()
            Log().info("Connection to RabbitMQ successfully")
        except:
            Log().error("Connection to RabbitMQ error", exc_info=True)

    def publish(self, sop_class, orthanc_instance_id):
        if not self.check_connection():
            self.connect()
        try:
            self.channel.queue_declare(queue = f"{config.queue_uid[sop_class]}", durable = True)
            self.channel.basic_publish(exchange = '', routing_key = f"{config.queue_uid[sop_class]}", body = json.dumps(orthanc_instance_id))
            Log().info(f"{orthanc_instance_id} publish to queue")
        except:
            Log().error("Publish to queue error", exc_info=True)
    
    def close_connection(self):
        self.connection.close()
        Log().info("Close connection to RabbitMQ")