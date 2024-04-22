from structures import RedBlackTree, HashMap
from player import Player
import fortnite_api
import time
import csv
import os


def get_api_data(username):
    player_data = api.stats.fetch_by_name(username)
    game_modes_data = player_data.raw_data['stats']['all']

    filtered_data = {'username': username}
    for mode in ['solo', 'duo', 'squad', 'ltm']:
        mode_data = game_modes_data.get(mode, {})
        # Data filtering
        filtered_data[mode] = {
            'score': mode_data.get('score', 0),
            'wins': mode_data.get('wins', 0),
            'kills': mode_data.get('kills', 0),
            'kd': mode_data.get('kd', 0),
            'matches': mode_data.get('matches', 0),
            'winrate': mode_data.get('winRate', 0),
            'minutes_played': mode_data.get('minutesPlayed', 0)
        }

    return Player(username, 0, 0, filtered_data["solo"]["kd"], filtered_data["solo"]["winrate"], 0, 0,
            filtered_data["solo"]["minutes_played"],
            0, 0, filtered_data["duo"]["kd"], filtered_data["duo"]["winrate"], 0, 0,
            filtered_data["duo"]["minutes_played"],
            0, 0, 0, 0, 0, 0, 0,
            0, 0, filtered_data["squad"]["kd"], filtered_data["squad"]["winrate"], 0,
            0, filtered_data["squad"]["minutes_played"],
            0, 0, 0, filtered_data["ltm"]["kd"], filtered_data["ltm"]["winrate"], 0,
            0, filtered_data["ltm"]["minutes_played"])


print("Welcome to Fortnite Academy!"
" This program uses ordered and unordered maps to store and compare your data to our dynamic dataset.")
print("\nBuilding datasets from CSV...")
# this file contains the main operations and sends them to app.py lol

tree = RedBlackTree()
hash_map = HashMap(2150)
# setting the hashmap with this value will prevent it from resizing while it's being built, speeding it up

# your API key should be stored as an environment variable
api_key = os.environ.get('api_key')
api = fortnite_api.FortniteAPI(api_key)

# read csv
with open("Fortnite_players_stats.csv", 'r', encoding='utf-8') as file:
    # skip the first line, it's not valid data
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
    print("Time to Build Tree: ", round((tree_elapsed_time * 1000), 2), "ms")

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
    print("Time to Build Hashmap: ", round((hashmap_elapsed_time * 1000), 2), "ms")

# menu loop
while True:
    print()
    try:
        number = int(input("Menu:\n0. Exit\n1. Insert Player\n2. Analyze Player\n"
                           "3. Delete Player\n4. Display Highest UNICODE Player\n\n"))
    except ValueError:
        print("Invalid input!")
        continue
    if number == 0:
        break
    elif number == 1:
        name = input("Choose a Player to Insert:\n")
        to_insert = get_api_data(name)

        tree_start_time = time.perf_counter()
        tree.insert(to_insert)
        tree_end_time = time.perf_counter()
        tree_elapsed_time = tree_end_time - tree_start_time
        print("\nTree Insert: ", round((tree_elapsed_time * 1000000), 2), "μs")

        hashmap_start_time = time.perf_counter()
        hash_map.insert(to_insert)
        hashmap_end_time = time.perf_counter()
        hashmap_elapsed_time = hashmap_end_time - hashmap_start_time
        print("Hashmap Insert: ", round((hashmap_elapsed_time * 1000000), 2), "μs")

    elif number == 2:
        name = input("Choose a Player to Analyze:\n")

        tree_start_time = time.perf_counter()
        acc = tree.tree_search(name)
        tree_end_time = time.perf_counter()
        tree_elapsed_time = tree_end_time - tree_start_time
        print("\nTree Search: ", round((tree_elapsed_time * 1000000), 2), "μs")

        hashmap_start_time = time.perf_counter()
        hash_map.get(name)
        hashmap_end_time = time.perf_counter()
        hashmap_elapsed_time = hashmap_end_time - hashmap_start_time
        print("Hashmap Search: ", round((hashmap_elapsed_time * 1000000), 2), "μs")

        valid_acc = acc

        if acc is None:
            print("Account not found in database, making API call...\n")
            valid_acc = get_api_data(name)

        print("      ====Solo Stats====")
        print(f"Your KD: {valid_acc.kd[0]} | Avg KD: {tree.calculate_tree_avg_kd(0)}")
        print(f"Your WR: {valid_acc.wr[0]} | Avg WR: {tree.calculate_tree_avg_wr(0)}")
        print("      ====Duo Stats====")
        print(f"Your KD: {valid_acc.kd[1]} | Avg KD: {tree.calculate_tree_avg_kd(1)}")
        print(f"Your WR: {valid_acc.wr[1]} | Avg WR: {tree.calculate_tree_avg_wr(1)}")
        print("     ====Squad Stats====")
        print(f"Your KD: {valid_acc.kd[2]} | Avg KD: {tree.calculate_tree_avg_kd(2)}")
        print(f"Your WR: {valid_acc.wr[2]} | Avg WR: {tree.calculate_tree_avg_wr(2)}")
        print("      ====LTM Stats====")
        print(f"Your KD: {valid_acc.kd[3]} | Avg KD: {tree.calculate_tree_avg_kd(3)}")
        print(f"Your WR: {valid_acc.wr[3]} | Avg WR: {tree.calculate_tree_avg_wr(3)}")

        if acc is None:
            add_bool = input("\nWould you like to add this account to the dataset? Enter y/n\n")
            if add_bool == 'y' or add_bool == 'Y':
                tree_start_time = time.perf_counter()
                tree.insert(valid_acc)
                tree_end_time = time.perf_counter()
                tree_elapsed_time = tree_end_time - tree_start_time
                print("Tree Insert: ", round((tree_elapsed_time * 1000000), 2), "μs")

                hashmap_start_time = time.perf_counter()
                hash_map.insert(valid_acc)
                hashmap_end_time = time.perf_counter()
                hashmap_elapsed_time = hashmap_end_time - hashmap_start_time
                print("Hashmap Insert: ", round((hashmap_elapsed_time * 1000000), 2), "μs")

    elif number == 3:
        name = input("Choose a Player to Remove:\n")

        tree_start_time = time.perf_counter()
        tree.remove(name)
        tree_end_time = time.perf_counter()
        tree_elapsed_time = tree_end_time - tree_start_time
        print("Tree Delete: ", round((tree_elapsed_time * 1000000), 2), "μs")

        hashmap_start_time = time.perf_counter()
        hash_map.remove(name)
        hashmap_end_time = time.perf_counter()
        hashmap_elapsed_time = hashmap_end_time - hashmap_start_time
        print("Hashmap Delete: ", round((hashmap_elapsed_time * 1000000), 2), "μs")
    elif number == 4:
        tree_start_time = time.perf_counter()
        acc = tree.get_highest()
        tree_end_time = time.perf_counter()

        # print it now that it's been stored and the stopwatch is done
        print(f"The name ordered by UNICODE is \"{acc.name}\"\n")

        tree_elapsed_time = tree_end_time - tree_start_time
        print("Tree Fetch: ", round((tree_elapsed_time * 1000000), 2), "μs")

        hashmap_start_time = time.perf_counter()
        hash_map.get_highest_unicode()
        hashmap_end_time = time.perf_counter()
        print("Hashmap Fetch: ", round((hashmap_elapsed_time * 1000000), 2), "μs")
    else:
        print("Input not recognized!\n")
