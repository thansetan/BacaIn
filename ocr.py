import pytesseract
from PIL import Image


# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe' #path ke file tesseract.exe
def ocr(filename): #Image to Text
    text = pytesseract.image_to_string(Image.open(filename))
    return text