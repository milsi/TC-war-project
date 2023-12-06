class Player:
    def __init__(self, name , hand):
        self.name = name
        self.hand = hand

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = list(hand)

    def battle(self):
        card = self.hand[-1]
        print(f"player {self.name}: {card}")
        self.put_card_on_table()
        return card

    def war(self):
        open_card = self.hand[-2]
        closed_card = self.hand[-1]
        print(f"player {self.name}: [??? ???]")
        print(f"player {self.name}: {open_card}")
        for _ in [open_card, closed_card]:
            self.put_card_on_table()
        return [closed_card, closed_card]

    def put_card_on_table(self):
        self.hand.pop()