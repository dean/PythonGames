#Blackjack.py
#This is the class used to play the card game Blackjack.
from Card import Card
from Deck import Deck
from Player import Player
class Blackjack(object):
	def __init__(self, player = Player("")):
		self.player = player;
		self.deck = Deck()
		self.deck.create_default_deck()
		self.deck.shuffle()
	def print_player_name(self):
		print self.player.get_name()
	def print_hand(self, player = Player("")):
		print player.get_name()+"'s cards:"
		for c in player.get_hand():
			print c.get_name()
	def bust(self, player = Player("")):
		sum = 0
		for c in player.get_hand():
			sum += c.get_value()
			if(sum>21):
				return True
		return False
	def count_cards(self, cards):
		sum = 0
		ace = 0
		for c in cards:
			if c.get_val==11 :
				ace += 1
			else:
				sum += c.get_val()
		if ace>0: ## Aces have varying values
			for i in range(ace):
				if sum+11 > 21:
					sum+=1
				else:
					sum+=11
		return sum
	def hit(self, player = Player("")):
		self.deck.deal(1, player) 
	def should_hit(self, ai_card_val):
		return ai_card_val < 17
	def dist_winnings(self, player = Player("")):
		print "Congratulations to "+player.get_name()+" for winning this round!";
	def dist_winnings_equally(self, ai = Player("")):
		print "Tie! Winnings will be distributed equally"
	def play(self):
		ai = Player ("AI")
		self.deck.deal(2, self.player)
		self.deck.deal(2, ai)
		player_card_val = self.count_cards(self.player.get_hand())
		ai_card_val = self.count_cards(ai.get_hand())
		self.print_hand(self.player)
		while "yes" in raw_input("Do you want to hit?: ").lower():
			self.hit(self.player)
			player_card_val = self.count_cards(self.player.get_hand())
			if (player_card_val>21):
				print self.player.get_name()+" busted!"
				self.dist_winnings(ai)
				return
			self.print_hand(self.player)
		while self.should_hit(ai_card_val):
			self.hit(ai)
			ai_card_val = self.count_cards
			if(ai_card_val >21):
				print ai.get_name()+" busted!"
				self.dist_winnings(self.player)
				return
		self.print_hand(ai)
		if player_card_val > ai_card_val :
			self.dist_winnings(self.player)
		elif ai_card_val > player_card_val:
			self.dist_winnings(ai)
		else:
			self.dist_winnings_equalls(ai)
		return
	
		
	
		
