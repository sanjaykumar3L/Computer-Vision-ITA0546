import cv2

image = cv2.imread(
    "C:/Users/lsk87/OneDrive/Desktop/download (1).jpg",
    cv2.IMREAD_GRAYSCALE
)

if image is None:
    print("Image not found!")
    exit()

sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)

cv2.imshow("Original Image", image)
cv2.imshow("Sobel Y", sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()
