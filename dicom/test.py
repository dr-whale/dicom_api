from config import config
from pyorthanc import Orthanc
import pydicom, os, io
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pydicom.filebase import DicomFileLike, DicomIO, DicomBytesIO


uid = '1.2.40.0.13.1.83810804622686936871639634610207012379'

def image_create(study_uid):
    orthanc = Orthanc('http://localhost:8042', 'orthanc', 'orthanc')
    study_id = orthanc.post_tools_find(dict(Level = 'Study', Query = dict(StudyInstanceUID = study_uid)))[0]
    patient_id = orthanc.get_studies_id_patient(study_id)['MainDicomTags']['PatientID']
    instance = orthanc.get_studies_id_instances(study_id)[0]
    
    bytes_instance = orthanc.get_instances_id_file(instance['ID'])
    buffer = DicomBytesIO(bytes_instance)
    ds = pydicom.dcmread(buffer)

image_create(uid)