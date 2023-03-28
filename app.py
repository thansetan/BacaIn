from base64 import b64encode
from io import BytesIO

from flask import Flask, render_template, request
from langdetect import detect
from PIL import Image

import ocr

# terima file tertentu
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
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
            extracted_text = ocr.ocr(file) #Terapin OCR
            try:
                bahasa = detect(extracted_text) #detect bahasa
                msg = 'Berhasil'
                clr = 'blue'
                disabled = ''
            except:
                bahasa = 'en'
                msg = 'Gagal mendeteksi teks'
                clr = 'gold'
                disabled = 'disabled'
            sebaris = " ".join(extracted_text.splitlines()) #jadiin sebaris biar bacanya lancar
            hasil = sebaris.strip() #ilangin simbol g penting yg diakhir
            
            #Tampilin gambar tanpa perlu save
            img = Image.open(file)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            data = BytesIO()
            img.save(data, "JPEG")
            encoded_img = b64encode(data.getvalue())
            decoded_img = encoded_img.decode('utf-8')
            img_src = f"data:image/jpeg;base64,{decoded_img}"

            return render_template('bacain.html',
            msg=msg,
            hasil=hasil,
            img_src=img_src, 
            clr=clr, 
            bahasa=bahasa,
            disabled=disabled)
    elif request.method == 'GET':
        return render_template('bacain.html')
@app.route('/howtouse')
def howtouse():
    return render_template('howtouse.html')
if __name__ == '__main__':
    app.run()