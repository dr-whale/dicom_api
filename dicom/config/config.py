import os
from dotenv import load_dotenv
from .enum_uid import StudiUID
load_dotenv()

LOGGER_LEVEL = os.environ.get("LOGGER_LEVEL") or "INFO"
LOGGER_FILE_PATH = os.environ.get("LOGGER_FILE_PATH") or "default_log.log"

RABBIT_HOST = os.environ.get("RABBIT_HOST") or "localhost"

ORTHANC_HOST = os.environ.get("ORTHANC_HOST") or "localhost"
ORTHANC_PORT = os.environ.get("ORTHANC_PORT") or "8042"
ORTHANC_USER = os.environ.get("ORTHANC_USER") or "orthanc"
ORTHANC_PASS = os.environ.get("ORTHANC_PASS") or "orthanc"

class_uid = {StudiUID.CT: [
                        '1.2.840.10008.5.1.4.1.1.2',
                        '1.2.840.10008.5.1.4.1.1.2.1',
                        '1.2.840.10008.5.1.4.1.1.2.2'
                        ],
            StudiUID.MR: [
                        '1.2.840.10008.5.1.4.1.1.4',
                        '1.2.840.10008.5.1.4.1.1.4.1',
                        '1.2.840.10008.5.1.4.1.1.4.2',
                        '1.2.840.10008.5.1.4.1.1.4.3',
                        '1.2.840.10008.5.1.4.1.1.4.4'
                        ]
            }

queue_uid = {
            StudiUID.CT: 'ct_queue',
            StudiUID.MR: 'mr_queue'
            }