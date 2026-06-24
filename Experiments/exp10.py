import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error loading webcam")
    exit()

cv2.namedWindow("Webcam Video")

speed_factor = 1.0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Webcam Video", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('+'):
        speed_factor += 0.5

    elif key == ord('-'):
        speed_factor = max(0.5, speed_factor - 0.5)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
