###########
### AI Controller with HTTP abstracted away
###
### Space is a dict which will be persisted across calls
###
###########

def start_game(game, space):
	pass

def start_turn(game, space):
	# For now just end turn immediately
	game.end_turn()