
import cv2

video_path = r"C:\Users\sambe\Downloads\ITA0513_CV\video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video not found!")
else:
    print("Press 1 for slow motion, 2 for fast motion, q to quit")
    mode = 1

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Video", frame)
        delay = 100 if mode == 1 else 10
        key = cv2.waitKey(delay) & 0xFF

        if key == ord("1"):
            mode = 1
        elif key == ord("2"):
            mode = 2
        elif key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
