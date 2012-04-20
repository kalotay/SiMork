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

from game import RESOURCES, GENERATOR_COST, GENERATOR_IMPROVEMENT_COST, ROAD_COST

def start_game(db, game):
	print "Starting a game"

def start_turn(db, game):
	print "Taking my turn"
	taking_turn = True
	while taking_turn:
		while game.can_purchase_generator():
			generator_type = game.purchase_generator()
			print "Purchased %s" % generator_type

		while game.can_upgrade_generator():
			generator_type = game.upgrade_generator()
			print "Upgraded %s" % generator_type

		while game.can_purchase_road():
			game.purchase_road()
			print "Purchased road"

		# Can't do anything? maybe trade for it
		taking_turn = False


		def trade_for(requirements):
			request = {}
			offer = {}

			for resource in RESOURCES:
				if resource in requirements and requirements[resource] > game.resources[resource]:
					request[resource] = requirements[resource] - game.resources[resource]
				else:
					to_offer = game.resources[resource] - requirements.get(resource, 0)
					if to_offer > 0:
						offer[resource] = to_offer

			return game.trade(offer, request)

		if sum(game.generators.values()) < 5:
			# Can build generators - try to trade for them
			if trade_for(GENERATOR_COST):
				taking_turn = True
		if sum(game.improved_generators.values()) < 4:
			# Can improve one of our existing ones
			if trade_for(GENERATOR_IMPROVEMENT_COST):
				taking_turn = True
		
		# Let's just build a road
		if trade_for(ROAD_COST):
			taking_turn = True

	game.end_turn()

def end_game(db, game, error=None):
	if error:
		print "Something went wrong! %s" % error
	else:
		print "Game over"

def incoming_trade(db, game, offering, requesting):
	print "INCOMING TRADE"
	# As long as I'm gaining at least one resource more than I'm giving away, I'll accept
	if sum(offering.values()) > sum(requesting.values()):
		print "ACCEPTED"
		return True
	return False