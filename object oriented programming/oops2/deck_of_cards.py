import random






class Card():
    def __init__(self,suit,value):
        self.suit = suit 
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck():
    suits = ["Hearts","Diamonds","Clubs","Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self):
        self.no_of_cards = 52
        self.cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(suit,value))

    def count(self):
        self.no_of_cards = len(self.cards)
        return self.no_of_cards


    def __repr__(self):
        return f"Deck of {self.no_of_cards} cards"

    def _deal(self,num):
        cards_dealt = []
        if self.no_of_cards is 0:
            raise ValueError("All cards has been dealt.")
        elif num > self.no_of_cards:
            for _ in self.cards:
                cards_dealt.append(self.cards.pop())
                self.no_of_cards -= 1
            return cards_dealt
        else:
            for _ in range(num):
                cards_dealt.append(self.cards.pop())
                self.no_of_cards -= 1
            return cards_dealt
                
    def shuffle(self):
        if self.no_of_cards < 52:
            raise ValueError("Only full decks can be shuffled")
        random.shuffle(self.cards)

    def deal_card(self):
        a_card = self._deal(1)
        return a_card

    def deal_hand(self,hands):
        deal_cards = self._deal(hands)
        return deal_cards

    

d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards)
print(hand)
card2 = d.deal_card()
     




















