#import import
# from pydub.playback import play
# from pydub import AudioSegment
import pytesseract
from PIL import Image
# from gtts import gTTS
# from io import BytesIO
# from google_trans_new import google_translator

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe' #path ke file tesseract.exe
def ocr(filename): #Image to Text
    text = pytesseract.image_to_string(Image.open(filename))
    return text
# # def tts(teks): #Text to Speech
#     tts = gTTS(text=teks, lang='id')
#     fp = BytesIO()
#     tts.write_to_fp(fp)
#     fp.seek(0)
#     return fp
# def baca(fp): #Read text to speech
#     speak = AudioSegment.from_file(fp, format='mp3')
#     play(speak)
# def translate(teks): #Translate 
#     translator = google_translator()
#     translatean = translator.translate(teks, lang_tgt='id')
#     return translatean
# def bacain(teks): #Main
#     hasil_tts = tts(teks)
#     omong = baca(hasil_tts)