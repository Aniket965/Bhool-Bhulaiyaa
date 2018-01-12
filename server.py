from flask import Flask,render_template,Response,url_for
import camera

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True)