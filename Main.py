#Main.py
#This is the file used to start the game of Blackjack and debug different classes
from Blackjack import Blackjack
from Card import Card
from Deck import Deck
from Player import Player
p = Player("Dean")
b = Blackjack(p)
inp = "yes"
while "yes" in inp.lower():
	b.play()
	inp = raw_input("Do you want to keep playing?: ")