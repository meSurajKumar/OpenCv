import cv2
import numpy as np 

width,height = 250 , 350 ## we use this later

img = cv2.imread("OpenCV/card.jpg")
pts1 = np.float32([[13,123],[144,98],[50,298],[179,271]])
print(pts1) # To know we are getting the desire point values. Which we extract from the the image.

'''
pts1 = np.float32([[13,123],[144,98],[50,298],[179,271]])
 
 these are the points which are taken from the card-image (paint is used to get the pixel values ) 
 a = 13 , 123
 b = 144 , 98
 c = 50 , 298
 d = 179 , 271

'''
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
'''
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
 These are the point which are used to make the image dimensions.
'''
matrix = cv2.getPerspectiveTransform(pts1,pts2)
'''
matrix = cv2.getPerspectiveTransform(pts1,pts2)
 This is used for Geometric Transformations of Images from pts1 to pts2.
'''
imgoutput = cv2.warpPerspective(img,matrix,(width,height))
'''
imgoutput = cv2.warpPerspective(img,matrix,(width,height))

syntax :-
 cv2.warpPerspective(src, dst, dsize)

 Parameters:
 ->src (img): Source Image
 ->dst (matrix): output image that has the size dsize and the same type as src.
 ->dsize (width,height): size of output image 
'''
for x in range(0,4):
    cv2.circle(img, (pts1[x][0],pts1[x][1]),5,(255,0,0),cv2.FILLED)

'''
This is to plot the circle on the main-image the 
    (for loop is used to shoter the code ) 
    you can also do this in without for loop like :-
    cv2.circle(img, (pts1[0][0],pts1[0][1]),5,(255,0,0),cv2.FILLED)
    cv2.circle(img, (pts1[1][0],pts1[1][1]),5,(255,0,0),cv2.FILLED)
    cv2.circle(img, (pts1[2][0],pts1[2][1]),5,(255,0,0),cv2.FILLED)
    cv2.circle(img, (pts1[3][0],pts1[3][1]),5,(255,0,0),cv2.FILLED)

    points positions:-         [0],[1]   [0],[1]  [0],[1]  [0],[1]
For help :- pts1 = np.float32([[13,123],[144,98],[50,298],[179,271]])
     index positions:-           [0]       [1]     [2]       [3]

'''

cv2.imshow("card",img)
cv2.imshow("output",imgoutput) ## Now we can uncomment this (after img,matrix and imgoutput)
cv2.waitKey(0)