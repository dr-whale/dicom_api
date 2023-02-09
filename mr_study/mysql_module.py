from config import config
from lib import Log
import sqlalchemy as db

engine = db.create_engine(f"mysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}/{config.MYSQL_DB}")
connect = engine.connect()
metadata = db.MetaData() #extracting the metadata
table= db.Table('mr_table', metadata, autoload_with=engine) #Table object

def insert_row(full_info):
    try:
        query = db.insert(table).values(ID = full_info['orthanc_id'], InstanceUID = full_info['instance_uid'], 
                                        SeriesUID = full_info['series_uid'], StudyUID = full_info['study_uid'],
                                        Patient = full_info['patient'], Rows = full_info['rows'], Columns = full_info['columns']
                                        )
        Log().info("Instance import to database")
    except:
        Log().error("Instance not import", exc_info=True)
    connect.execute(query)
    connect.commit()

def check_orthanc_id(orthanc_id):
    query = connect.execute(db.select(table.c.ID)).all()
    result = orthanc_id in query
    return result