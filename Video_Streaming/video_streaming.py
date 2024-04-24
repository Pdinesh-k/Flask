from flask import Flask,render_template,Response,redirect
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def generate_frame():
    while(True):
        satisfied,frame = camera.read()
        if(not satisfied):
            break
        else:
            true,buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
            yield(b'--frame\r\n'b'Content-Type:image/jpeg\r\n\r\n'
                  +frame+b'\r\n')


           

@app.route('/')
def message():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frame(),mimetype='multipart/x-mixed-replace;boundary=frame') 


if(__name__ == '__main__'):
    app.run(debug=True)