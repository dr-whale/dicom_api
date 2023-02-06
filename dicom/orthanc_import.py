import os, pika
from pyorthanc import Orthanc
from lib import Log, Rabbit
from config import config

def orthanc_import(filename, sop_class, study_id):
   orthanc = Orthanc(f'http://{config.ORTHANC_HOST}:{config.ORTHANC_PORT}', config.ORTHANC_USER, config.ORTHANC_PASS)
   with open(f'tmp/{filename}', 'rb') as file:
      try:
         orthanc.post_instances(file.read())
         os.remove(file.name)
         Log().info(f'{file.name} import to Orthanc and remove from temp')
         Rabbit().publish(sop_class, study_id)
      except:
         Log().error("File not import to Orthanc", exc_info=True)

# body study_instance_uid / sop_instance_uid
# id исследования и инстанса

# channel.queue_declare(queue = f"{config.queue_uid[sop_class]}", durable = True)
# channel.basic_publish(exchange = '', routing_key = f"{config.queue_uid[sop_class]}", body = '')
# connection.close()