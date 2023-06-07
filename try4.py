import pytesseract
from PIL import Image
import cv2

im_file='data/try4.jpg'

im=Image.open(im_file)

print(im.size)

left = 500
top = 150
right = 1150
bottom = 450

im1 = im.crop((left, top, right, bottom)) 
im1=im1.rotate(-10)
im1.save("temp/try4_cr.jpg")


def ocr_core(file):
    text = pytesseract.image_to_string(Image.open(file))  
    return text

print(ocr_core('temp/try4_cr.jpg'))
