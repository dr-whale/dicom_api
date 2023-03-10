import os
from pydicom import dcmread
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from lib import Log, uid_checker, Rabbit, LocalAE
from orthanc_import import orthanc_import
from config import config
from image import image_create

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
            sop_class = uid_checker(str(dicom_info.SOPClassUID))
            if (sop_class != None):
                filename = secure_filename(file.filename)
                file.stream.seek(0)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                Log().info(f"Dicom file {filename} saved in temp")
                resp = jsonify({'message' : 'File successfully uploaded'})
                resp.status_code = 201
                orthanc_import(filename, sop_class)
            else:
                Log().warning(f"Wrong SOPClassUID {filename}")
        except:
            Log().error("File is not dicom", exc_info=True)
            resp = jsonify({'message' : 'File is no dicom'})
            resp.status_code = 400
    Rabbit().close_connection()
    return resp

@app.route('/move', methods=['GET'])
def get_move():
    patient_id = request.args.get('patient')
    try:
        LocalAE().move(patient_id)
        Log().info("C-Move success")
    except:
        Log().error("C-Move PACS Error", exc_info=True)
    return jsonify("C-Move success")

@app.route('/image', methods=['GET'])
def get_image():
    study_uid = request.args.get('study')
    try:
        image_create(study_uid)
        Log().info("Image Create")
    except:
        Log().error("Image Error", exc_info=True)
    return jsonify("Image create success")