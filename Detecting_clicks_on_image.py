import cv2
import numpy as np

def mouseClicks(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

img = cv2.imread("OpenCV/card.jpg")
cv2.imshow("Original image" , img)
cv2.setMouseCallback("Original image",mouseClicks)
cv2.waitKey(0)




