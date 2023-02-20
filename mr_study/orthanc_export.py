from lib import Log
from config import config
from pyorthanc import Orthanc


def orthanc_export(orthanc_instance_id):
    try:
        orthanc = Orthanc(f'http://{config.ORTHANC_HOST}:{config.ORTHANC_PORT}', config.ORTHANC_USER, config.ORTHANC_PASS)
        Log().info(f"Orthanc connection with id: {orthanc_instance_id}")
    except:
        Log().error("Orthanc connection error", exc_info=True)
    full_info = {}
    full_info['orthanc_id'] = orthanc_instance_id
    full_info['rows'] = int.from_bytes(orthanc.get_instances_id_content_tags_path('0028-0010', orthanc_instance_id), "little")
    full_info['columns'] = int.from_bytes(orthanc.get_instances_id_content_tags_path('0028-0010', orthanc_instance_id), "little")
    full_info['patient'] = orthanc.get_instances_id_patient(orthanc_instance_id)['MainDicomTags']['PatientID']
    full_info['study_uid'] = orthanc.get_instances_id_study(orthanc_instance_id)['MainDicomTags']['StudyInstanceUID']
    full_info['series_uid'] = orthanc.get_instances_id_series(orthanc_instance_id)['MainDicomTags']['SeriesInstanceUID']
    full_info['instance_uid'] = orthanc.get_instances_id(orthanc_instance_id)['MainDicomTags']['SOPInstanceUID']
    return full_info