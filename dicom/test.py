from config import config
from pyorthanc import Orthanc

study_uid = '1.2.40.0.13.1.83810804622686936871639634610207012379'

orthanc = Orthanc('http://localhost:8042', 'orthanc', 'orthanc')

#instances = orthanc.get_instances()
#for instance in instances:
#    print(orthanc.get_instances_id(instance))

studies = orthanc.get_studies()
for study in studies:
    if(orthanc.get_studies_id(study)['MainDicomTags']['StudyInstanceUID'] == study_uid):
        instance = orthanc.get_studies_id_instances(study)