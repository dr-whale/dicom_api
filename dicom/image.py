from config import config
from pyorthanc import Orthanc
import pydicom
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pydicom.filebase import DicomBytesIO


def image_create(study_uid):
    orthanc = Orthanc(f'http://{config.ORTHANC_HOST}:{config.ORTHANC_PORT}', config.ORTHANC_USER, config.ORTHANC_PASS)
    study_id = orthanc.post_tools_find(dict(Level = 'Study', Query = dict(StudyInstanceUID = study_uid)))[0]
    patient_id = orthanc.get_studies_id_patient(study_id)['MainDicomTags']['PatientID']
    instance = orthanc.get_studies_id_instances(study_id)[0]
    
    bytes_instance = DicomBytesIO(orthanc.get_instances_id_file(instance['ID']))

    new_image = pydicom.dcmread(bytes_instance).pixel_array.astype(float)
    scaled_image = np.uint8((np.maximum(new_image, 0) / new_image.max()) * 255.0)
    image = Image.fromarray(scaled_image)

    font = ImageFont.truetype('font.ttf', 25)
    drawer = ImageDraw.Draw(image)
    drawer.text((50, 100), patient_id, font = font, fill='white')

    image.save(f'/app/png/{patient_id}.png', 'png')