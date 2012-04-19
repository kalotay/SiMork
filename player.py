#############
### Sample AI
#############

from bottle import post, put
from bottle import request, abort, run

from storage import use_db
import logic

import thread

def use_game(f):
	def inner_func(db, session_id, *args, **kwargs):
		if not request.json:
			abort(400, 'Must use Content-type of application/json')
		game = db.get(session_id)
		if not game or not game.get('type') == 'game':
			abort(400, 'Not a valid game')
		return f(db, game, *args, **kwargs)
	return inner_func

@put('/game/:session_id')
@use_db
def start_game(db, session_id):
	game = {"type": "game", "id": session_id, "space": {}}
	db.save(game)
	return {"status": "success"}

@post('/game/:session_id/start_turn')
@use_db
@use_game
def start_turn(db, game):
	def run_turn():
		#something
		pass
	thread.start_new_thread(run_turn, ())
	return {"status": "success"}

run(host='localhost', port=8099, reloader=True)