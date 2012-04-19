import json
from httplib2 import Http

GENERATOR_COST = {
	"brick": 1,
	"lumber": 1,
	"wool": 1,
	"grain": 1
}

GENERATOR_IMPROVEMENT_COST = {
	"ore": 3,
	"grain": 2
}

ROAD_COST = {
	"brick": 1,
	"lumber": 1
}

class Game(object):
	def __init__(self, game, player):
		self.game = game
		self.storage = game['storage']
		self.resources = player['resources']
		self.generators = player['generators']
		self.improved_generators = player['improved_generators']
		self.roads = player['roads']

	def request(self, resource, body=None, method='POST'):
		http = Http()

		if not body:
			body = {}

		body['player_id'] = self.game['id']
		body = json.dumps(body)

		response, data = http.request("%s/%s" % (self.game['endpoint'], resource), method=method, body=body, headers={"Content-type": "application/json"})

		if response.status != 200:
			print "Error ", data
			return False

		data = json.loads(data)
		if 'player' in data:
			player = data['player']
			self.resources = player['resources']
			self.generators = player['generators']
			self.improved_generators = player['improved_generators']
			del data['player']
		return data

	def can_purchase_road(self):
		for resource in ROAD_COST:
			if self.resources[resource] < ROAD_COST[resource]:
				return False
		return True

	def purchase_road(self):
		self.request('purchase_road')

	def can_purchase_generator(self):
		if sum(self.generators.values()) > 5:
			return False # Can't have more than 5 generators

		for resource in GENERATOR_COST:
			if self.resources[resource] < GENERATOR_COST[resource]:
				return False
		return True

	def purchase_generator(self):
		data = self.request('purchase_road')

	def can_upgrade_generator(self):
		if sum(self.improved_generators.values()) > 4:
			return False # Can't have more than 5 generators

		if sum(self.generators.values()) < 1:
			return False # Need an original generator to upgrade

		for resource in GENERATOR_IMPROVEMENT_COST:
			if self.resources[resource] < GENERATOR_IMPROVEMENT_COST[resource]:
				return False
		return True

	def upgrade_generator(self, generator_type=None):
		if not generator_type:
			for generator in self.generators:
				if self.generators[generator] > 0:
					generator_type = generator
					break

		if not generator_type:
			return False

		data = self.request('upgrade_generator', {"generator_type": generator_type})

	def end_turn(self):
		self.request('end_turn')