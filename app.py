from flask import Flask, render_template, Response
import cv2
import numpy as np
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return 'web app testing on aws server'
@app.route('/test')
def test():
    return render_template("index.html")

def gen_frames():
    #url = 'https://youtu.be/Jh4QFaPmdss'
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps=30
    out = cv2.VideoWriter('video.avi', fourcc, fps,(int(width), int(height)))
    while True:
        ret, image = camera.read()
        #cv2.imshow(image)
        #out.write(image)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        ret, buffer = cv2.imencode('.jpg', image)
        grame = buffer.tobytes()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.release()
    out.release()
    cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
