from cv2 import imshow
from flask import Flask, render_template, Response

import cv2


app=Flask(__name__)
#vc = cv2.VideoCapture(0)


def live_stream():  
    vc = cv2.VideoCapture(0)
    while True:
        success, frame = vc.read()  # read the camera frame
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
                 cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 5)
                 roi_gray = gray[y:y+w, x:x+w]
                 roi_color = frame[y:y+h, x:x+w]

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/stream')
def stream(): 
    return Response(live_stream(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)