
import cv2


vc = cv2.VideoCapture(0)


cv2.namedWindow("Live-Feed")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

rval, frame = vc.read()


img_counter = 0

while vc.isOpened():
    rval, frame = vc.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

   
    cv2.imshow("Live-Feed", frame)
   
    key = cv2.waitKey(20)

    if key == ord('q'):
        break
    elif key == 32:
        # SPACE pressed
        img_name = "opencv_frame.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

cv2.destroyWindow("Live-Feed")
vc.release()
