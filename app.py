from flask import Flask, jsonify, render_template, send_file
from main import data

app = Flask(__name__, template_folder='.')  # static_url_path=''


@app.route('/')
def index():
    return render_template("tempo.html")


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
