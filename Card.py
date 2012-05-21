#Card.py
#This class represents a Card used for card games.
class Card(object):
	def __init__(self, value, suit, game):
		self.value = value
		self.suit = suit
		self.game = game
		self.cName = self.set_name(value, suit)
		if game=="Blackjack":
			ace=False 
			if value>10: #Workaround because elif isn't working correctly
				if value==14:
					ace = True
				self.value=10
			if ace:
				self.value+=1
	def set_name(self, value, suit):
		if value>10:
			arr = ["Jack", "Queen", "King", "Ace"]
			return arr[value%10 - 1]+" of "+suit
		return str(value)+" of "+suit
	def get_name(self):
		return self.cName
	def get_val(self):
		return self.value
	def str_val(self):
		print "value of "+self.get_name()+" is "+str(self.val)
			