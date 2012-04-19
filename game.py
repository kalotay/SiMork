import json
from httplib2 import Http

class Game(object):
	def __init__(self, game):
		self.game = game
		self.storage = game['storage']

	def request(self, resource, body=None, method='POST'):
		http = Http()

		if not body:
			body = {}
		
		body['player_id'] = self.game['id']
		body = json.dumps(body)

		return http.request("%s/%s" % (self.game['endpoint'], resource), method=method, body=body, headers={"Content-type": "application/json"})

	def end_turn(self):
		self.request('end_turn')