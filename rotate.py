import cv2
import numpy as np
img= cv2.imread("cropped.jpg",0)
rows,cols = img.shape[:2]
M= cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst= cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("dst", dst)
cv2.imwrite("rotate.jpg", dst)
cv2.waitKey(0)
