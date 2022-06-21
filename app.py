from flask import Flask, render_template, request, jsonify
import time


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')


@app.route('/train', methods=['POST'])  # This will be called from UI
def train_model():
    if (request.method=='POST'):
        time.sleep(10)
        return jsonify({'status': 'success'})



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000,debug=True)
