import serverless_wsgi ##Load module serverless for the lambda
from flask import Flask, request, jsonify ##Load flask module for web base app
import logging
from time import strftime

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
LOGGER.addHandler(console_handler)

app = Flask(__name__)

#list of key value to be queried
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


"""Flask routing to return OK when uri /health_check is requested
# Defining a function to return Ok every time /health_check is requested"""
@app.route("/health_check")
def index():
    return "OK"

"""defining on methods GET and POST on uri /games
defining a function when /games is requested
if the request method is GET
If the length value of list games_list is greater than 0
 use module jsonify to return all the value of the game_list when /games is requested
return 404 if request methods is not GET and length is not > than 0
if the request method is POST
increment the id of the new post value"""

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

@app.after_request
def after_request(response):
   timestamp = strftime('[%Y-%b-%d %H:%M]')
   LOGGER.info('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
   return response

"""Define function handler for the lambda to trigger on event
##module serverless_wsgi is loaded to handle the request on events triggering function"""
def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)