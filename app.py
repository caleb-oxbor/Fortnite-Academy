from flask import Flask, jsonify, render_template, send_file
from main import data
import fortnite_api
import os

app = Flask(__name__, template_folder='.')  # static_url_path=''

api_key = os.environ.get('api_key')
api = fortnite_api.FortniteAPI(api_key)


@app.route('/')
def index():
    return render_template("welcome.html")


@app.route('/image')
def image():
    return render_template("index.html")


@app.route('/favicon.ico')
def favicon():
    return '', 204


@app.route('/<path:filename>')
def static_files(filename):
    return send_file(filename)


@app.route('/data')
def get_data():
    return jsonify(data)


if __name__ == '__main__':
    app.run()
