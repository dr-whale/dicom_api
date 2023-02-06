import pika
from .class_description import Singleton
from config import config
from flask import jsonify

class Rabbit (metaclass=Singleton):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(config.RABBIT_HOST))
        self.channel = self.connection.channel()

    def publish(self, sop_class, study_id):
        self.channel.queue_declare(queue = f"{config.queue_uid[sop_class]}", durable = True)
        self.channel.basic_publish(exchange = '', routing_key = f"{config.queue_uid[sop_class]}", body = jsonify(study_id))
    
    def close_connection(self):
        self.connection.close()

    def __getattr__(self, name):
        if hasattr(self.logger, name):
            return getattr(self.logger, name)
        else:
            return getattr(self, name)