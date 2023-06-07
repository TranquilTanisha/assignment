import cv2
import numpy as np

img=cv2.imread('data/lambo.png')
kernel=np.ones((5,5), np.uint8)

cv2.imshow('lambo',img)
cv2.imwrite('temp/lambo/lambo1.png', img)
cv2.waitKey(0)

#to grey an image
imGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("temp/lambo/gray.png", imGray)
cv2.imshow("Grey", imGray)

#to blurr an image
imgBlur=cv2.GaussianBlur(imGray, (7,7), 0)
cv2.imwrite("temp/lambo/blur.png", imgBlur)
cv2.imshow("Blur", imgBlur)

#to detect the border of an image
imgCanny=cv2.Canny(img, 200, 100)
cv2.imwrite("temp/lambo/canny.png", imgCanny)
cv2.imshow("Canny Image", imgCanny)

#to dialate an image
imgDialation=cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imwrite("temp/lambo/dialate.png", imgDialation)
cv2.imshow("Dialated Image", imgDialation)

#to read an image correctly
imgEroded=cv2.erode(imgDialation, kernel, iterations=1)
cv2.imwrite("temp/lambo/eroded.png", imgEroded)
cv2.imshow("Eroded Image", imgEroded)

print(img.shape)

#to resize the img
#resize to smaller than original
imgResize=cv2.resize(img, (300, 450))
cv2.imwrite("temp/lambo/smaller.png",imgResize)
cv2.imshow("Resized Image", imgResize)

#resize to the screen size
imgResize=cv2.resize(img, (1920, 1080))
cv2.imwrite("temp/lambo/larger.png",imgResize)
cv2.imshow("Resized Image", imgResize)

#to crop an image, height and width
imgCropped=img[100:300, 200:500]
cv2.imwrite("temp/lambo/cropped.png", imgCropped)
cv2.imshow("Cropped Image", imgCropped)


#insert shapes
#to draw a rectangle
im1=img.copy()
cv2.rectangle(im1, (100,100), (350,250), (10,100,255), 3)

#to draw a circle
cv2.circle(im1, (200,300), 50, (70,140,20), 3)
cv2.imshow("Image", im1)
cv2.imwrite("temp/lambo/shapes.png", im1)

#join images
imgHor=np.hstack((img, img))
cv2.imwrite("temp/lambo/horizontal.png", imgHor)
cv2.imshow("Hor", imgHor)

imgVer=np.vstack((img, img))
cv2.imwrite("temp/lambo/vertical.png", imgVer)
cv2.imshow("Ver", imgVer)

cv2.waitKey(0)