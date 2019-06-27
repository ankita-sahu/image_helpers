import cv2
import numpy as np
img= cv2.imread('pic1.jpg',1)
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def drawKeypoints(img, keypoints, color):
	for kp in keypoints:
		x,y= kp.pt
		cv2.circle(img,(int(x),int(y)),8,color)
fast = cv2.FastFeatureDetector_create()
brief= cv2.xfeatures2d.BriefDescriptorExtractor_create()
keypoints= fast.detect(gray,None)
keypoints, descriptors = brief.compute(gray, keypoints)
print("keypoints detected", len(keypoints))

drawKeypoints(img, keypoints, (0,0,255)) 

cv2.imshow('Feature Method - BRIEF', img)
cv2.imwrite('briefwrite.jpg',img)
cv2.waitKey()
cv2.destroyAllWindows()
