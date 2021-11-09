import cv2
import numpy as np

## This is for the webcam or external camera.
cap = cv2.VideoCapture(0)

def empty(a):
    pass

cv2.namedWindow("Parameter")
cv2.createTrackbar("Threshold1","Parameter",81,255,empty)
cv2.createTrackbar("Threshold2","Parameter",151,255,empty)


## The contour function....

def getContours(video,videocontours):
    contours , hierarchy = cv2.findContours(video , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(video,contours,-1,(255,0,255),7)



while True:
    capturing , video = cap.read()
    # video = cv2.cvtColor(video, cv2.COLOR_GRAY2BGR)
    video = cv2.resize(video,(440,350))
    videocontours = video.copy()
    videoblur = cv2.GaussianBlur(video,(7,7),1)
    videoGray = cv2.cvtColor(videoblur,cv2.COLOR_BGR2GRAY)
    patch = cv2.cvtColor(videoGray,cv2.COLOR_GRAY2BGR) ## patch for gray image

    threshold1 = cv2.getTrackbarPos("Threshold1","Parameter")
    threshold2 = cv2.getTrackbarPos("Threshold2","Parameter") 

    videocanny = cv2.Canny(videoGray,threshold1,threshold2) ## have only 1 or 2 channel
    videocanny1 = cv2.cvtColor(videocanny,cv2.COLOR_GRAY2BGR) ## patch for canny image now it ahs 3 channels
    kernel = np.ones((5,5))
    videoDil = cv2.dilate(videocanny1,kernel,iterations =1 )
    getContours(videoDil,videocontours)

    
    stack = np.hstack((video,videocanny1,videocontours,patch))
    
    # cv2.imshow("webcamera" , video)
    cv2.imshow("webcamera" , stack)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()