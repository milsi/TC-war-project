import pydealer
from player import Player


deck = pydealer.Deck()
deck.shuffle()

player1_deck = deck.deal(26)
player2_deck = deck.deal(26)

player_1 = Player("Abe", player1_deck)
player_2 = Player("Barb", player2_deck)
