###########
### AI Controller with HTTP abstracted away
###########

from baselogic import BaseLogic

class Logic(BaseLogic):
	def start_game():
		pass
	
	def start_turn(self):
		# For now just end turn immediately
		self.end_turn()