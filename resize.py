import cv2
import numpy as np
img= cv2.imread('test1.jpg')
res= cv2.resize(img, dsize=(40,30), interpolation= cv2.INTER_CUBIC)
cv2.imwrite('test2.jpg',img)
i=cv2.imread('test2.jpg')
cv2.imshow("IMAGE",i)
cv2.waitKey(0)
