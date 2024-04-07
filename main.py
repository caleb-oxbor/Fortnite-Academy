from collections import OrderedDict
from player import Player
import time
import csv


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


    # design red-black tree to represent ordered map

    # come up with a custom hashing function for unordered map
