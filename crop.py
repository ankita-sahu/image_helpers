import cv2
img = cv2.imread("trial.jpg")

cropped = img[0:100, 0:200]
cv2.imshow("cropped", cropped)
cv2.imwrite('cropped.jpg',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
