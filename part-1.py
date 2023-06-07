from PIL import Image

im_file='main.jpg'

im=Image.open(im_file)

# im.show()

#saving the image
im.save('temp\img1.jpg')

# Setting the points for cropped image 
left = 562
top = 2460
right = 1043
bottom = 2560
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im=im.rotate(5)
im1 = im.crop((left, top, right, bottom)) 
  
# Shows the image in image viewer 
# im1.show()

im1.save("temp/segmented2.jpg")

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
img = Image.open('temp/segmented2.jpg') 

def ocr_core(img):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(img))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core('temp/segmented2.jpg'))
