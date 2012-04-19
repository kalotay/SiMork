#############
### Sample AI
#############

from bottle import post, put, delete
from bottle import request, abort, run

from storage import use_db
import logic

import thread
from game import Game

def use_game(f):
	def inner_func(db, session_id, *args, **kwargs):
		g = db.get(session_id)
		if not g or not g.get('type') == 'game':
			abort(400, 'Not a valid game')

		if not 'json' in kwargs:
			if not request.json:
				abort(400, 'Must use Content-type of application/json')
			kwargs['json'] = request.json

		if not 'player' in kwargs['json']:
			abort(400, 'Must pass "player"')
		
		player = kwargs['json']['player']
		del kwargs['json']

		game = Game(g, player)
		return f(db, game, *args, **kwargs)
	return inner_func

@put('/game/:session_id')
@use_db
def start_game(db, session_id):
	game = {"type": "game", "id": session_id, "storage": {}, "endpoint": request.json['endpoint']}
	db.save(game)
	return {"status": "success"}

@post('/game/:session_id/start_turn')
@use_db
@use_game
def start_turn(db, game):
	def run_turn():
		logic.start_turn(db, game)
	thread.start_new_thread(run_turn, ())
	return {"status": "success"}

@delete('/game/:session_id')
@use_db
@use_game
def end_game(db, game):
	if request.json and 'error' in request.json:
		def run_end():
			logic.end_game(db,game,request.json['error'])
	else:
		def run_end():
			logic.end_game(db,game)
	return {"status": "success"}

run(host='localhost', port=8099, reloader=True)