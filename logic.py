###########
### AI Controller with HTTP abstracted away
###
### DB is a wrapper for whatever storage is backing the AI
### Use this for storage across games
###
### game contains a "storage" object which is a dict which will be
### persisted after returning
###
###########

def start_game(db, game):
	print "Starting a game"

def start_turn(db, game):
	# For now just end turn immediately
	print "Taking my turn"
	game.end_turn()

def end_game(db, game, error=None):
	if error:
		print "Something went wrong! %s" % error
	else:
		print "Game over"
