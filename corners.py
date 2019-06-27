import cv2
import numpy as np
image= cv2.imread('trial.jpg', 1)
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray= np.float32(gray)
corners= cv2.cornerHarris(gray, 3,3, 0.1)

kernel= np.ones((7,7), np.uint8)
corners= cv2.dilate(corners, kernel, iterations=4)

image[corners > 0.05*corners.max() ] = [255,0,0]

cv2.imshow('Harris corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
