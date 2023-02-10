from config import config
from lib import Log
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import sqlalchemy as db

class Base(DeclarativeBase):
    pass

class MRInfo(Base):
    __tablename__ = "mr_table"

    id = db.Column("ID", db.String, primary_key = True)
    instance_uid = db.Column("InstanceUID", db.String)
    series_uid = db.Column("SeriesUID", db.String)
    study_uid = db.Column("StudyUID", db.String)
    patient = db.Column("Patient", db.String)
    rows = db.Column("Rows", db.Integer)
    columns = db.Column("Columns", db.Integer)

    def __init__(self, id, instance_uid, series_uid, study_uid, patient, rows, columns):
        self.id = id
        self.instance_uid = instance_uid
        self.series_uid = series_uid
        self.study_uid = study_uid
        self.patient = patient
        self.rows = rows
        self.columns = columns
    
    def __repr__(self):
            return f"{self.id} {self.instance_uid} {self.series_uid} {self.study_uid} {self.patient} {self.rows} {self.columns}"

engine = db.create_engine(f"mysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}/{config.MYSQL_DB}")
Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind = engine)
session = Session()

def id_checker(orthanc_id):
    if (session.query(session.query(MRInfo).filter_by(id=orthanc_id).exists()).scalar()):
        Log().info("Equal ID")
        return False
    return True

def insert_row(info):
    try:
        if id_checker(info['orthanc_id']):
            mrinfo = MRInfo(info['orthanc_id'], info['instance_uid'], info['series_uid'], 
                            info['study_uid'],info['patient'], info['rows'], info['columns'])
            session.add(mrinfo)
            session.commit()
            Log().info(f"{info['orthanc_id']} save in Database")
    except:
        Log().error("Error save in Database", exc_info=True)