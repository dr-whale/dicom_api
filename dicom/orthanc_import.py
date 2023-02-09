import os
from pyorthanc import Orthanc
from lib import Log, Rabbit
from config import config

def orthanc_import(filename, sop_class):
   orthanc = Orthanc(f'http://{config.ORTHANC_HOST}:{config.ORTHANC_PORT}', config.ORTHANC_USER, config.ORTHANC_PASS)
   with open(f'tmp/{filename}', 'rb') as file:
      try:
         orthanc_instance_id = orthanc.post_instances(file.read())['ID']
         os.remove(file.name)
         Log().info(f'{file.name} import to Orthanc and remove from temp')
      except:
         Log().error("File not import to Orthanc", exc_info=True)
      Rabbit().publish(sop_class, orthanc_instance_id)
