from structures import RedBlackTree, HashMap
from player import Player
import fortnite_api
import time
import csv
import os

# this file contains the main operations and sends them to app.py

player_vec = []
tree = RedBlackTree()
hash_map = HashMap()

api_key = os.environ.get('api_key')
api = fortnite_api.FortniteAPI(api_key)


# read csv
with open("Fortnite_players_stats.csv", 'r', encoding='utf-8') as file:
    # create reader objects and skip the first line for each
    csv_reader = csv.reader(file)
    next(csv_reader)

    tree_start_time = time.perf_counter()

    for row in csv_reader:
        tree.insert(Player(row[0],
                           row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                           row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                           row[15], row[16], row[17], row[18], row[19], row[20], row[21],
                           row[22], row[23], row[24], row[25], row[26], row[27], row[28],
                           row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36]))

    tree_end_time = time.perf_counter()
    tree_elapsed_time = tree_end_time - tree_start_time
    # storing time in milliseconds, perfect for seeing the difference between the structures
    print("time to build tree: ", round((tree_elapsed_time * 1000), 2), "ms")

    file.seek(0)
    next(csv_reader)

    for row in csv_reader:
        player_vec.append(Player(row[0],
                                 row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                 row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                                 row[15], row[16], row[17], row[18], row[19], row[20], row[21],
                                 row[22], row[23], row[24], row[25], row[26], row[27], row[28],
                                 row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36]))

    file.seek(0)
    next(csv_reader)

    hashmap_start_time = time.perf_counter()

    for row in csv_reader:
        hash_map.insert(Player(row[0],
                               row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                               row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                               row[15], row[16], row[17], row[18], row[19], row[20], row[21],
                               row[22], row[23], row[24], row[25], row[26], row[27], row[28],
                               row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36]))

    hashmap_end_time = time.perf_counter()
    hashmap_elapsed_time = hashmap_end_time - hashmap_start_time
    print("time to build hashmap: ", round((hashmap_elapsed_time * 1000), 2), "ms")

tree_solo_kd = round(tree.calculate_tree_avg(), 2)
print("average tree solo KD:", tree_solo_kd)

hashmap_solo_kd = round(hash_map.calculate_hashmap_avg(), 2)
print("average hashmap solo KD:", hashmap_solo_kd)

test_player_obj = api.stats.fetch_by_name("CringyBruh")
print(test_player_obj.raw_data)

labels = ['A', 'B', 'C']
values = [10, 20, 15]
data = {'labels': labels, 'values': values}
