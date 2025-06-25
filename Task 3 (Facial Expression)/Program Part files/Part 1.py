import cv2
import time

a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
b = cv2.VideoCapture(0)

if not b.isOpened():
    print("ERROR: PLEASE CHECK YOUR CAMERA. IT IS UNABLE TO ACCESS :<(")
    exit()

last_detection_time = time.time()
time_limit = 40

window_name = 'Face Detector'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

while True:
    c_rec, d_image = b.read()
    if not c_rec or d_image is None:
        print("Failed to capture image. Exiting.")
        break

    clean_image = d_image.copy()
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    f = a.detectMultiScale(e, scaleFactor=1.3, minNeighbors=5)

    if len(f) > 0:
        last_detection_time = time.time()
        for (x, y, w, h) in f:
            cv2.rectangle(d_image, (x, y), (x + w, y + h), (100, 200, 300), 5)

    cv2.imshow(window_name, d_image)

    key = cv2.waitKey(1) & 0xFF

    
    if cv2.getWindowProperty(window_name, cv2.WND_PROP_AUTOSIZE) == -1:
        print("Window closed by user. Exiting.")
        break

    if key == ord('s'):
        image_filename = f"captured_from_face_dector_{int(time.time())}.jpg"
        cv2.imwrite(image_filename, clean_image)
        print(f"Image saved as {image_filename}")
    elif key == 27 or key == ord('q') or key == ord('Q'):
        break

    if time.time() - last_detection_time > time_limit:
        print("No face detected for 40 seconds. Stopping the program.")
        break

b.release()
cv2.destroyAllWindows()
