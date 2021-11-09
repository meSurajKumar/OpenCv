import cv2
import numpy as np

## This is for color detection.

frame_width = 200
frame_height = 200

cap = cv2.VideoCapture(0)
cap.set(3,frame_width)
cap.set(4,frame_height)

def blank(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE MIN","HSV",0,179,blank)
cv2.createTrackbar("HUE MAX","HSV",179,179,blank)
cv2.createTrackbar("SAT MIN","HSV",0,255,blank)
cv2.createTrackbar("SAT MAX","HSV",255,255,blank)
cv2.createTrackbar("VALUE MIN","HSV",0,255,blank)
cv2.createTrackbar("VALUE MAX","HSV",255,255,blank)

while True:
    capturing , video = cap.read()
    videoHSV = cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
    '''
    1st we have converted BGR to HSV because it is easy to work with HSV.
    H :-HUE = color.
    S :-saturation = How pure the color is.
    v :-value = How bright the color is 
    '''
    H_MIN = cv2.getTrackbarPos("HUE MIN","HSV")
    H_MAX = cv2.getTrackbarPos("HUE MAX","HSV")
    S_MIN = cv2.getTrackbarPos("SAT MIN","HSV")
    S_MAX = cv2.getTrackbarPos("SAT MAX","HSV")
    V_MIN = cv2.getTrackbarPos("VALUE MIN","HSV")
    V_MAX = cv2.getTrackbarPos("VALUE MAX","HSV")
    # print(H_MIN)
    lower = np.array([H_MIN,S_MIN,V_MIN])
    upper =np.array([H_MAX,S_MAX,V_MAX])
    mask = cv2.inRange(videoHSV,lower,upper)
    result = cv2.bitwise_and(video,video,mask = mask)
    cv2.imshow("webcamera" , video)
    cv2.imshow("MASK" , mask)
    cv2.imshow("result" , result)
    # cv2.imshow("HSV webcam" , videoHSV)
    cv2.waitKey(1)

