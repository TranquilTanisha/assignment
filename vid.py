import cv2
import numpy as np

frameWidth=640
frameHeight=480
cap=cv2.VideoCapture("data\sample-1.mp4")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('temp/vid/output.avi', fourcc, 20.0, (640,480))

while True:
    success, img=cap.read()
    img=cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Video", img)
    if cv2.waitKey(21) & 0xFF ==ord('q'):
        break

    if success==True:
        img = cv2.flip(img,0)
        out.write(img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()

out.release()

cv2.destroyAllWindows()
    
