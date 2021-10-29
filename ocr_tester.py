import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/John Chen/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

print(pytesseract.image_to_string(Image.open('test_img1.png')))
print(pytesseract.image_to_string(Image.open('purchase_snip.png')))
print(pytesseract.image_to_string(Image.open('locked_snip.png')))