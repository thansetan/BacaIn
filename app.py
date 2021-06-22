import os
from flask import Flask, render_template, request
from ocr import *
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'static/uploads/'

# terima file tertentu
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app = Flask(__name__)


#cek ekstensi file
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def homepage():
    return render_template('index.html')
@app.route('/kelompok')
def kelompok():
    return render_template('anggota.html')
@app.route('/bacain', methods=['GET', 'POST'])
def bacain():
    global extracted_text
    if request.method == 'POST':
        if 'file' not in request.files: #kalo gaada file
            return render_template('bacain.html', msg='Gagal, belum memilih file', clr='red')
        file = request.files['file']
        if file.filename == '': #kalo gaada file 
            return render_template('bacain.html', msg='Gagal, belum memilih File', clr='red')

        if file and allowed_file(file.filename):
            extracted_text = ocr(file)
            file.seek(0)
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return render_template('bacain.html',
            msg='Berhasil',
            extracted_text=extracted_text,
            img_src=UPLOAD_FOLDER + file.filename, clr='blue')
            return extracted_text
    elif request.method == 'GET':
        return render_template('bacain.html')
@app.route('/howtouse')
def howtouse():
    return render_template('howtouse.html')

# @app.route('/bacain')
# def bacain():
#     bacain(extracted_text)
#     return ('nothing')

if __name__ == '__main__':
    app.run()