from flask import Flask, jsonify, render_template, send_file
from structures import RB_Tree, Hash_Map
from player import Player
import time
import csv


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
    labels = ['A', 'B', 'C']
    values = [10, 20, 45]
    data = {'labels': labels, 'values': values}
    return jsonify(data)


if __name__ == "__main__":

    player_vec = []
    tree = RB_Tree()
    hash_map = Hash_Map()

    # read csv
    with open("Fortnite_players_stats.csv", 'r', encoding='utf-8') as file:

        # create reader object and skip the first line
        csv_reader1 = csv.reader(file)
        csv_reader2 = csv.reader(file)
        csv_reader3 = csv.reader(file)

        next(csv_reader1)
        next(csv_reader2)
        next(csv_reader3)

        tree_start_time = time.perf_counter()

        for row in csv_reader1:

            tree.insert(Player(row[0],
            row[1], row[2], row[3], row[4], row[5], row[6], row[7],
            row[8], row[9], row[10], row[11], row[12], row[13], row[14],
            row[15], row[16], row[17], row[18], row[19], row[20], row[21],
            row[22], row[23], row[24], row[25], row[26], row[27], row[28],
            row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36]))

        tree_end_time = time.perf_counter()
        tree_elapsed_time = tree_end_time - tree_start_time
        print("time to build tree: ", (tree_elapsed_time * 1000000), "μs")

        for row in csv_reader2:

            player_vec.append(Player(row[0],
            row[1], row[2], row[3], row[4], row[5], row[6], row[7],
            row[8], row[9], row[10], row[11], row[12], row[13], row[14],
            row[15], row[16], row[17], row[18], row[19], row[20], row[21],
            row[22], row[23], row[24], row[25], row[26], row[27], row[28],
            row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36]))

        hashmap_start_time = time.perf_counter()

        for row in csv_reader3:

            hash_map.insert(Player(row[0],
            row[1], row[2], row[3], row[4], row[5], row[6], row[7],
            row[8], row[9], row[10], row[11], row[12], row[13], row[14],
            row[15], row[16], row[17], row[18], row[19], row[20], row[21],
            row[22], row[23], row[24], row[25], row[26], row[27], row[28],
            row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36]))

        hashmap_end_time = time.perf_counter()
        hashmap_elapsed_time = hashmap_end_time - hashmap_start_time
        print("time to build hashmap: ", (hashmap_elapsed_time * 1000000), "μs")

    print("Done!")
    app.run()
    # type " $env:FLASK_APP="main.py" " to get it working in terminal
