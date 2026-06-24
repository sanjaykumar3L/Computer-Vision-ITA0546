import cv2

image = cv2.imread("C:/Users/lsk87/OneDrive/Desktop/maserati.jpg")

rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()