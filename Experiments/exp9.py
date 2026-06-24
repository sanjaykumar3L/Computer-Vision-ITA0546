import cv2

def play_video(video_path, speed=1.0):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error loading video")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video", frame)

        delay = int(1000 / (fps * speed))

        if cv2.waitKey(delay) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

play_video("C:/Users/lsk87/OneDrive/Desktop/video.mp4", speed=1.0)
