import whisper
from flask import Flask, flash, request, redirect, url_for
import os

app = Flask(__name__)
upload_folder = "Upload_folder"
app.config['UPLOAD_FOLDER'] = upload_folder


@app.route("/", methods=['GET', 'POST'])
def greet():
    if os.path.isdir(upload_folder):
        print(f'{os.getcwd()}')
    else:
        os.mkdir(upload_folder)
        print(f'{os.getcwd()}')
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        model = whisper.load_model("tiny")
        result = model.transcribe(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return f'''
        <title>You have uploaded {file.filename}!</title>
        <h1>You have uploaded {file.filename}!</h1>
        <br />
        <p><b>Here's your transcript!</b></p><br />
        <p>{result["text"]}</p>
        '''
    else:
        return '''<!doctype html>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form action='' method="POST" enctype="multipart/form-data">
    <p><input type='file' name='file' multiple=''>
    <input type='submit' value='upload'>
    </p>

</form>
'''
