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
	print "Taking my turn"
	
	# while game.can_purchase_generator():
	# 	generator_type = game.purchase_generator()
	# 	print "Purchased %s" % generator_type

	# while game.can_upgrade_generator():
	# 	generator_type = game.upgrade_generator()
	# 	print "Upgraded %s" % generator_type

	while game.can_purchase_road():
		game.purchase_road()
		print "Purchased road"

	game.end_turn()

def end_game(db, game, error=None):
	if error:
		print "Something went wrong! %s" % error
	else:
		print "Game over"
