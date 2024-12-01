import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not accessible!")
else:
    _, frame = cap.read()
    if frame is not None:
        print("Camera working!")
    cap.release()
