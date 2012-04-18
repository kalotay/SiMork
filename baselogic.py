from httplib2 import Http

class BaseLogic(object):
	def __init__(self, game_runner, game_id):
		self.http = Http()
		self.game_url = game_runner + '/game/%i' + game_id
		self.start_game()

	def start_game(self):
		pass

	def start_turn(self):
		pass

	def request(self, resource, method='GET', body=None, headers={"Content-type": "application/json"}):
		if body and not isinstance(body, basestring):
			body = json.dumps(body)

		return self.http.request("%s/%s" % (self.game_url, resource), method=method, body=body, headers=headers)

	def end_turn(self):
		self.request('/end_turn', 'POST')