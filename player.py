#############
### Sample AI
#############

from bottle import post, put
from bottle import request, abort

import logic

# Incoming

games = {}

def use_game(f):
	def inner_func(game_id, *args, **kwargs):
		if not request.json:
			abort(400, 'Must use Content-type of application/json')
			game = games[request.json['endpoint']][game_id]
		return f(game, *args, **kwargs)
	return inner_func

@put('/game/:game_id')
def start_game(game_id):
	endpoint = request.json['endpoint']
	if not endpoint in games:
		games[endpoing] = {}

	games[game_id] = logic.Logic(request.json['endpoint'], game_id)
	return {"status": "success"}

@post('/game/:game_id/start_turn')
@use_game
def start_turn(game):
	game.start_turn()

run(host='localhost', port=8099, reloader=True)