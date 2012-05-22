#Player.py
#This class represents a player of a game.
from Card import Card
class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []
	def give_cards(self, cards):
		for card in cards:
			self.hand.append(card)
	def get_name(self):
		return self.name
	def get_hand(self):
		return self.hand
	def get_hand_size(self):
		return len(self.hand)
	def return_hand(self):
		temp = []
		for c in self.hand:
			temp.append(c);
		self.hand[:] = []
		return temp;
		
