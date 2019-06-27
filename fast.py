import cv2
import numpy as np

image= cv2.imread('pic1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def drawKeypoints(image, keypoints, color):
	for kp in keypoints:
		x,y=kp.pt
		cv2.circle(image, (int (x), int (y)), 6, color)
		#print(x,y)

		
fast = cv2.FastFeatureDetector_create()
keypoints= fast.detect(gray, None)
print ("number of keypoints detected:", len(keypoints))
drawKeypoints(image ,keypoints, (255,0,0))
cv2.imshow('FAST', image)
cv2.imwrite('fastwrite.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

