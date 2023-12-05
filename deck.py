import pydealer


deck = pydealer.Deck()

player1_deck = deck.deal(26)
player2_deck = deck.deal(26)

player1_card = player1_deck[-1]
player2_card = player1_deck[1]

result = player1_card < player2_card

#print(result)

class Player:
    def __init__(self, name , card):
        self.name = name
        self.card = card
        
    def show_player_card():
        
        

    
    
player1 = Player("Tom", player1_deck)