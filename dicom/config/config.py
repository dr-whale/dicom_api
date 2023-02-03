import os
from dotenv import load_dotenv
load_dotenv()

LOGGER_LEVEL = os.environ.get("LOGGER_LEVEL") or "INFO"
LOGGER_FILE_PATH = os.environ.get("LOGGER_FILE_PATH") or "default_log.log"

ORTHANC_HOST=os.environ.get("ORTHANC_HOST") or "http://localhost"
ORTHANC_PORT=os.environ.get("ORTHANC_PORT") or "8042"
ORTHANC_USER=os.environ.get("ORTHANC_USER") or "orthanc"
ORTHANC_PASS=os.environ.get("ORTHANC_PASS") or "orthanc"