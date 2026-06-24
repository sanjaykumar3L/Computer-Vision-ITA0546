import cv2
image = cv2.imread("C:/Users/lsk87/OneDrive/Desktop/maserati.jpg")
cv2.imshow('original',image)
cv2.waitKey(0)
x = 100
y = 100
dx = 10
dy = 10
while True:
    cv2.imshow("Moving Image", image)
    cv2.moveWindow("Moving Image", x, y)

    x += dx
    y += dy

    if cv2.waitKey(50) & 0xFF == 27:  # ESC key
        break

cv2.destroyAllWindows()
