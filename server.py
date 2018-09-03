from flask import Flask,render_template,Response,url_for,jsonify,send_from_directory
from generateMap import imagetoLines
import cv2

w = 1246
h = 886
img = cv2.imread('loll.jpeg')
horlines,vertlines = imagetoLines(img,w,h)
app = Flask(__name__,static_url_path='')
@app.route('/')
def index():
    return render_template('index.html',value={"w":w,"h":h,"horlines":horlines,"vertlines":vertlines})

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

@app.route('/vr')
def vr():
    horlines,vertlines = imagetoLines(img,w,h)
    return jsonify(str(horlines))


if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True)