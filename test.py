import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

## The contour function....

def empty(a):
    pass


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",0,255,empty)
cv2.createTrackbar("Threshold2","Parameters",255,255,empty)
cv2.createTrackbar("Area","Parameters",5000,50000,empty)

'''
The sliders are introduce for adjustments.
'''
def getContours(video,videocontours):
    contours , hierarchy = cv2.findContours(video , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area","Parameter")
        if area > areaMin:
            cv2.drawContours(videocontours,cnt,-1,(255,0,255),7)
            perimeter = cv2.arcLength(cnt,True)
            '''
            perimeter = cv2.arcLength(cnt,True) :-To find out the corner points so we use have
            to first findout the length of our contours (cnt). so we use the (cv2.arcLength function)
            And the true is mean :- the contour is closed.

            And this will gives us the length of the perimeter and from which we can approximate
            which type of shape it is.

            '''
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            '''
            For approximation we use the (approxPolyDP) we will give it our contour (cnt)
            and the resolution of (0.02*perimeter) and (True) is meant that the contour is closed.
            And by this (approx) we can say this is rectangle , triangle or square.
            '''
            print(len(approx)) ## and here we printout the length of the (approx).
            x,y,w,h = cv2.boundingRect(approx)
            '''
            x,y,w,h = cv2.boundingRect(approx) :- we are creting a bounding rectangle because 
            it is not necessary that our shape must be a square or rectangle.          
            '''
            cv2.rectangle(videocontours,(x,y),(x+w,y+h),(0,255,0),5)
            '''
            we can simply display the bounding rectangle by :- 
            cv2.rectangle(videocontours,(x,y),(x+w,y+h),(0,255,0),5)
            {(x,y)} is the initial points and {(x+w,y+h)} are the final points.
            
            '''
            cv2.putText(videocontours, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                        (0, 255, 0), 2)
            '''
            To display the points of objects on the screen            
            '''
            cv2.putText(videocontours, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)
            '''
            To display the points of objects on the screen            
            '''

while True:
    sucesss , video = cap.read()
    # video1 = cv2.resize(video,(420,350))
    videocontours = video.copy() ## This to get rid from error (videocontours variable is not define)
    
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")


    videocanny = cv2.Canny(video,threshold1,threshold2)

    kernel = np.ones((5,5))
    videoDil = cv2.dilate(videocanny,kernel,iterations =1 )
    '''
    videocanny , what is kernal , why videoDil all are explained in previous code/videos.
    '''
    getContours(videoDil,videocontours)## Drawing contours on videoDil.


    # cv2.imshow("dil",videoDil)
    cv2.imshow("contours",videocontours)

    # cv2.imshow("canny",videocanny)
    cv2.imshow("webcam",video)
    cv2.waitKey(1)
