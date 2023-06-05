import serverless_wsgi ##Load module serverless for the lambda
from flask import Flask, request, jsonify ##Load flask module for web base app

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
] #list of key value to be queried

@app.route("/health_check") #Flask routing to return OK when uri /health_check is requested
def index(): # Defining a function to return Ok every time /health_check is requested
    return "OK"

@app.route("/games", methods=['GET', 'POST'])  #defining on methods GET and POST on uri /games
def games(): #defining a function when /games is requested
    if request.method == 'GET': #if the request method is GET
        if len(games_list) > 0: #If the length value of list games_list is greater than 0
            return jsonify(games_list)  ## use module jsonify to return all the value of the game_list when /games is requested
        else:
            'No games found', 404 #return 404 if request methods is not GET and length is not > than 0

    if request.method == 'POST': #if the request method is POST
        new_name = request.form['name']
        new_company = request.form['company']
        ID = games_list [-1] ['id'] + 1 #increment the id of the new post value

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
def handler(event, context): ## Define function handler for the lambda to trigger on event
    return serverless_wsgi.handle_request(app, event, context) ##module serverless_wsgi is loaded to handle the request on events triggering function
