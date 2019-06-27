import cv2
import numpy as np
image= cv2.imread('pic1.jpg', 1)
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
def drawKeypoints(gray, keypoints, color):
        for kp in keypoints:
                x,y= kp.pt
                cv2.circle(gray,(int(x),int(y)),8,color)
orb= cv2.ORB_create()
keypoints= orb.detect(gray, None)

keypoints, descriptors= orb.compute(gray, keypoints)
print("number of keypoints:", len(keypoints))

drawKeypoints(image, keypoints, (0,255,0))
cv2.imshow("ORB", image)
cv2.imwrite("ORBwrite.jpg", image)
cv2.waitKey()
cv2.destroyAllWindows()

