import os
from pydicom import dcmread
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from lib import Log, uid_checker
from orthanc_import import orthanc_import
from config import config

""" ds = dcmread("mrt/PA000001/ST000001/SE000001/IM000001")
ds = dcmread(path)
elem = ds['SOPClassUID']
print(elem.value)
print(ds.SOPClassUID)
print(ds.__class__ is pydicom.FileDataset) """

# CT Image Storage = 1.2.840.10008.5.1.4.1.1.2
# MR Image Storage = 1.2.840.10008.5.1.4.1.1.4
# CT и MR в env 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'tmp'

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        Log().warning("Request without file")
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    files = request.files.getlist("file")
    Log().info("Dicom files list requested")
    for file in files:
        try:
            dicom_info = dcmread(file)
            sop_class = uid_checker(dicom_info['SOPClassUID'])
            if (sop_class != None):
                filename = secure_filename(file.filename)
                file.stream.seek(0)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                Log().info(f"Dicom file {filename} saved in temp")
                resp = jsonify({'message' : 'File successfully uploaded'})
                resp.status_code = 201
                orthanc_import(filename, sop_class, dicom_info['StudyID'])
            else:
                Log().warning(f"Wrong SOPClassUID {filename}")
        except:
            Log().error("File is not dicom",exc_info=True)
            resp = jsonify({'message' : 'File is no dicom'})
            resp.status_code = 400
    return resp
