import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.cards = []
        for i in suits:
            for j in values:
                self.cards.append((Card(i, j)))
                print(self.cards)

    def mix(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
            print(self.cards)
        else:
            return "The deck is not full"

    def deal(self):
        if len(self.cards)== 0:
            raise ValueError('The deck is empty')
        else:
            deal_card = self.cards[-1]
            del self.cards[-1]
            return f"The {deal_card} is removed from the deck"
        
  
    
    


d = Deck()
print(d.mix())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())

 
