import os
from pyorthanc import Orthanc
from lib import Log
from config import config

def orthanc_import():
   orthanc = Orthanc(f'{config.ORTHANC_HOST}:{config.ORTHANC_PORT}', config.ORTHANC_USER, config.ORTHANC_PASS)
   for filename in os.listdir('tmp'):
      with open(f'tmp/{filename}', 'rb') as file:
         try:
            orthanc.post_instances(file.read())
            os.remove(file.name)
            Log().info(f'{file.name} import to Orthanc and remove from temp')
         except:
            Log().error("File not import to Orthanc", exc_info=True)