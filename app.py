from flask import Flask, jsonify, render_template, send_file, request
from main import data
import fortnite_api
import os

app = Flask(__name__, template_folder='.')  # static_url_path=''

api_key = os.environ.get('api_key')
api = fortnite_api.FortniteAPI(api_key)


@app.route('/')
def index():
    return render_template("index.html")


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


@app.route('/player_stats', methods=['POST'])
def player_stats():
    if request.method == 'POST':
        username = request.form['username']
        # Keeping log of username
        print(f"Received username: {username}")

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
            return jsonify(filtered_data)
        except Exception as e:
            # Logging exception
            print(f"Exception occurred: {e}")
            return jsonify({'error': 'Failed to retrieve data', 'message': str(e)})


if __name__ == '__main__':
    app.run()
