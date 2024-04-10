from flask import Flask, jsonify, render_template, send_file
# from collections import OrderedDict edit: we probs wont need this cause we're building from scratch
from player import Player
import time
import csv


app = Flask(__name__, template_folder='.') # static_url_path=''
@app.route('/')
def index():
    return render_template("tempo.html")

@app.route('/<path:filename>')
def static_files(filename):
    return send_file(filename)

@app.route('/data')
def get_data():
    data = {'first' : 1, 'second' : 2}
    return jsonify(data)


if __name__ == "__main__":

    player_vec = []

    # read csv
    with open("Fortnite_players_stats.csv", 'r', encoding='utf-8') as file:

        # create reader object and skip the first line
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            player_vec.append(Player(row[0],
            row[1], row[2], row[3], row[4], row[5], row[6], row[7],
            row[8], row[9], row[10], row[11], row[12], row[13], row[14],
            row[15], row[16], row[17], row[18], row[19], row[20], row[21],
            row[22], row[23], row[24], row[25], row[26], row[27], row[28],
            row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36]))

    print("Done!")
    # app.run(debug=True) uncomment to run the thing, but its better to do "flask run" in terminal

    # design red-black tree to represent ordered map
    # https://blog.boot.dev/python/red-black-tree-python/

    # come up with a custom hashing function for unordered map