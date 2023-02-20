from config import config
from pyorthanc import Orthanc, find
import pydicom, os, json
import numpy as np
from PIL import Image


uid = '1.2.40.0.13.1.83810804622686936871639634610207012379'

orthanc = Orthanc('http://localhost:8042', 'orthanc', 'orthanc')

""" studies = orthanc.get_studies()
for study in studies:
    if(orthanc.get_studies_id(study)['MainDicomTags']['StudyInstanceUID'] == study_uid):
        instance = orthanc.get_studies_id_instances(study)[0]
        #pydicom.dcmread(orthanc.get_instances_id_file(instance['ID']))

        msg = orthanc.get_instances_id_file(instance['ID'])
        f = open('tmp.dcm', 'wb')
        f.write(msg)
        f.close()

        new_image = pydicom.dcmread('tmp.dcm').pixel_array.astype(float)
        scaled_image = np.uint8((np.maximum(new_image, 0) / new_image.max()) * 255.0)
        final_image = Image.fromarray(scaled_image)
        final_image.show()

        os.remove('tmp.dcm') """

#resp_data = json.dumps(dict(Level = 'Study', Query = dict(StudyInstanceUID = uid)))
responce = orthanc.post_tools_find(dict(Expand = True, Level = 'Study', Query = dict(StudyInstanceUID = uid)))
print(responce)

"""   {
    "Level": "Studies",
    "Expand": true,
    "Query": {
      "StudyDate": "20220502"
    },
    "RequestedTags": ["PatientName", "PatientID", "StudyDescription", "StudyDate", "StudyInstanceUID", "ModalitiesInStudy", "NumberOfStudyRelatedSeries"]
  }' """
