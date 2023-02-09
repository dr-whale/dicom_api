import os
from dotenv import load_dotenv
load_dotenv()

LOGGER_LEVEL = os.environ.get("LOGGER_LEVEL") or "INFO"
LOGGER_FILE_PATH = os.environ.get("LOGGER_FILE_PATH") or "default_log.log"

RABBIT_HOST = os.environ.get("RABBIT_HOST") or "localhost"

ORTHANC_HOST=os.environ.get("ORTHANC_HOST") or "localhost"
ORTHANC_PORT=os.environ.get("ORTHANC_PORT") or "8042"
ORTHANC_USER=os.environ.get("ORTHANC_USER") or "orthanc"
ORTHANC_PASS=os.environ.get("ORTHANC_PASS") or "orthanc"

MYSQL_HOST = os.environ.get("MYSQL_HOST") or "localhost"
MYSQL_USER = os.environ.get("MYSQL_USER") or "root"
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD") or "root"
MYSQL_DB = os.environ.get("MYSQL_DB") or "mysql"