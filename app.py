from flask import Flask, jsonify, render_template, send_file, request
from main import data, tree, hash_map
import fortnite_api
import logging
import time
import os

logging.basicConfig(level=logging.INFO)

app = Flask(__name__, template_folder='.')  # static_url_path=''

api_key = os.environ.get('api_key')
api = fortnite_api.FortniteAPI(api_key)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/image')
def image():
    return render_template("welcome.html")


@app.route('/favicon.ico')
def favicon():
    return '', 204


@app.route('/<path:filename>')
def static_files(filename):
    return send_file(filename)


@app.route('/data')
def get_data():
    return jsonify(data)


@app.route('/player_stats', methods=['POST'])
def player_stats():
    try:
        if request.method == 'POST':

            skibidi = request.json

            username = skibidi.get('username')
            print(username)
            # Keeping log of username
            logging.info(f"Received username: {username}")

            # if the search fails for the tree and hashmap, it will return None so check that

            # tree search
            tree_search_start = time.perf_counter()
            p_info = tree.tree_search(username)
            tree_search_end = time.perf_counter()
            tree_elapsed_search = tree_search_end - tree_search_start
            print("time to search tree: ", round((tree_elapsed_search * 1000000), 2), "μs")

            # map search
            map_search_start = time.perf_counter()
            hash_map.get(username)
            map_search_end = time.perf_counter()
            map_elapsed_search = map_search_end - map_search_start
            print("time to search map: ", round((map_elapsed_search * 1000000), 2), "μs")

            if p_info is None:
                try:
                    player_data = api.stats.fetch_by_name(username)

                    if 'stats' in player_data.raw_data and 'all' in player_data.raw_data['stats']:
                        game_modes_data = player_data.raw_data['stats']['all']
                    else:
                        # Logging only when the expected is not found
                        print("Expected 'stats' and 'all' keys not found in response")
                        return jsonify({'error': 'Stats data not found in API response'})

                    filtered_data = {'username': username}  # Include username in the response
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

                        test_solo_kd = filtered_data["solo"]["kd"]
                        test_solo_wr = filtered_data["solo"]["winrate"]

                    # return jsonify(filtered_data)
                except Exception as e:
                    # Logging exception
                    print(f"Exception occurred: {e}")
                    return jsonify({'error': 'Failed to retrieve data', 'message': str(e)})
            else:

                player_data = {
                    # kd and wr
                    "solo_kd": p_info.kd_solo,
                    "solo_wr": p_info.wr_solo,
                    "duo_kd": p_info.kd_duo,
                    "duo_wr": p_info.wr_duo,
                    "squad_kd": p_info.kd_squad,
                    "squad_wr": p_info.wr_squad,
                    # mins played
                    "solo_mins": p_info.mins_solo,
                    "duo_mins": p_info.mins_duo,
                    "squad_mins": p_info.mins_squad,
                    "ltm_mins": p_info.mins_ltm
                }

                test_solo_kd = player_data["solo_kd"]
                test_solo_wr = player_data["solo_wr"]

                # return jsonify(player_data)

            # this json should contain the data for all 7 graphs
            to_json = [
                {
                    'label': 'solo_kd',
                    'data': {
                        'labels': ['Your KD', 'AVG KD'],
                        'values': [test_solo_kd, tree.calculate_tree_avg()]
                    }
                },
                {
                    'label': 'solo_wr',
                    'data': {
                        'labels': ['Your WR', 'AVG WR'],
                        'values': [test_solo_wr, 3.0] # change second value here, its wrong
                    }
                }
            ]

            print('reached here')
            return jsonify(to_json)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'Internal Server Error'})


if __name__ == '__main__':
    app.run()
