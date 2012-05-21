#Card.py
#This class represents a Deck of cards used for card games.
from Card import Card
from Player import Player
import random
class Deck(object):
	def __init__(self):
		self.arr = []
	def create_default_deck(self):
		suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
		idx = 0
		for i in range(1, 5, 1):
			for k in range(2, 15, 1):
				c = Card(k, suits[i-1], "Blackjack")
				self.arr.append(c)
	def print_deck(self):
		print "Is this working?"
		for c in self.arr:
			c.print_card()
	def shuffle(self):
		for i in range(len(self.arr)):
			rand = int(random.random()*(len(self.arr)))
			holder = self.arr[i]
			self.arr[i] = self.arr[rand]
			self.arr[rand] = holder
	def deal(self, num_cards, player = Player("")):
		player.give_cards(self.arr[len(self.arr)-num_cards:])
		del(self.arr[len(self.arr)-num_cards:])
	def get_top_card(self):
		return self.arr.pop(-1)
	def size(self):
		return len(self.arr)
	def get(self, idx):
		return self.arr(idx)
	
	
		
		
		