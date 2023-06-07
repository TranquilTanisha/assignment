import cv2
import numpy as np
from PIL import Image
import pytesseract

img = cv2.imread("data/try3.jpg")

# convert input image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cascade = cv2.CascadeClassifier('data\haarcascade_russian_plate_number.xml')

plates = cascade.detectMultiScale(gray, 1.2, 5)

for (x,y,w,h) in plates:
   cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
   gray_plates = gray[y:y+h, x:x+w]
   color_plates = img[y:y+h, x:x+w]
   
   cv2.imwrite('temp/try3_cr.jpg', gray_plates)
   # cv2.imshow('Numberplate.jpg', color_plates)
cv2.imshow('Numberplate.jpg', gray_plates)

def ocr_core(file):
    text = pytesseract.image_to_string(Image.open(file))  
    return text

print(ocr_core('temp/try3_cr.jpg'))

cv2.waitKey(0)
cv2.destroyAllWindows()