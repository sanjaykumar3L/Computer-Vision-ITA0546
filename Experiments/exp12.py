import cv2
import numpy as np

img = cv2.imread("C:/Users/lsk87/OneDrive/Desktop/images.jpg")

pts1 = np.float32([[50,50],[200,50],[50,200],[200,200]])
pts2 = np.float32([[10,100],[200,50],[100,250],[250,300]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img, matrix, (500,500))

cv2.imshow("Original", img)
cv2.imshow("Perspective Transform", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
