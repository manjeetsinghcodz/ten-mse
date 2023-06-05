import serverless_wsgi
from flask import Flask, request, jsonify

app = Flask(__name__)

games_list = [
    {
        "id": 0,
        "name": "Vice City",
        "company": "Rockstar Games",
    },
    {
        "id": 1,
        "name": "San Andreas",
        "company": "Rockstar Games",
    }
]

@app.route("/health_check")
def index():
    return "NOK"

@app.route("/games", methods=['GET', 'POST'])
def games():
    if request.method == 'GET':
        if len(games_list) > 0:
            return jsonify(games_list)
        else:
            'No games found', 404

    if request.method == 'POST':
        new_name = request.form['name']
        new_company = request.form['company']
        ID = games_list [-1] ['id'] + 1

        new_objects = {
            'id': ID,
            'name': new_name,
            'company': new_company,
        }
        games_list.append(new_objects)
        return jsonify(games_list), 201
@app.route("/games/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def single_game(id):
    if request.method == 'GET':
        for game in games_list:
            if game['id'] == id:
                return jsonify(game)
            pass
    if request.method == 'PUT':
        for game in games_list:
            if game['id'] == id:
                game['name'] = request.form['name']
                game['company'] = request.form['company']
                updated_game = {
                    'id': id,
                    'name': game['name'],
                    'company': game['company']
                }
                return jsonify(updated_game)
    if request.method == 'DELETE':
        for index, game in enumerate(games_list):
            if game['id'] == id:
                games_list.pop(index)
                return jsonify(games_list)
def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
