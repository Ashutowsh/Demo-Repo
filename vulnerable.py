# vulnerable_upload.py

import os
from flask import Flask, request

app = Flask(_name_)

UPLOAD_FOLDER = '/tmp/uploads'

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    
    os.system("file " + file_path)

    return "File uploaded successfully"

if _name_ == '_main_':
    app.run(debug=True)