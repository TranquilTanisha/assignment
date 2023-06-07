import pytesseract
from PIL import Image
import cv2

im_file='data/try1.jpg'

im=Image.open(im_file)

print(im.size)

# Setting the points for cropped image 
left = 630
top = 630
right = 1070
bottom = 740

# im=im.rotate(5)
im1 = im.crop((left, top, right, bottom)) 
im1.show()

im1.save("temp/try1_cr.jpg")

def ocr_core(file):
    text = pytesseract.image_to_string(Image.open(file))  
    return text

print(ocr_core('temp/try1_cr.jpg'))
