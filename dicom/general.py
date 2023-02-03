import os
from pydicom import dcmread
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from lib import Log
from orthanc_import import orthanc_import

""" ds = dcmread("mrt/PA000001/ST000001/SE000001/IM000001")
ds = dcmread(path)
elem = ds['SOPClassUID']
print(elem.value)
print(ds.SOPClassUID)
print(ds.__class__ is pydicom.FileDataset) """


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
            dcmread(file)
            filename = secure_filename(file.filename)
            file.stream.seek(0)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            Log().info(f"Dicom file {filename} saved in temp")
            resp = jsonify({'message' : 'File successfully uploaded'})
            resp.status_code = 201
        except:
            Log().error("File is not dicom",exc_info=True)
            resp = jsonify({'message' : 'File is no dicom'})
            resp.status_code = 400
    orthanc_import()
    return resp
