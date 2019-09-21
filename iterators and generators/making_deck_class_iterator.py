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
        # self.cards = [Card(value,suit) for suit in suts for value in values]  easy way
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(suit,value))

    def __repr__(self):
        return f"Deck of {self.no_of_cards} cards"

    def __iter__(self):  # here we made our deck class iterator
        return iter(self.cards)

    def count(self):
        self.no_of_cards = len(self.cards)
        return self.no_of_cards


    

    def _deal(self,num):
        count = self.count()
        cards_dealt = []
        if count is 0:
            raise ValueError("All cards has been dealt.")
        elif num > count:
            for _ in self.cards:
                cards_dealt.append(self.cards.pop())
                self.no_of_cards -= 1
            return cards_dealt
        else:
            for _ in range(num):
                cards_dealt.append(self.cards.pop())
                self.no_of_cards -= 1
            return cards_dealt



    '''        a easy way

	def _deal(self, num):
		count = self.count()
		actual = min([count,num])
		if count == 0:
			raise ValueError("All cards have been dealt")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards
        '''
                
    def shuffle(self):
        if self.no_of_cards < 52:
            raise ValueError("Only full decks can be shuffled")
        random.shuffle(self.cards)

    def deal_card(self):
       return self._deal(1)[0]
        

    def deal_hand(self,hands):
        return self._deal(hands)

    
my_deck = Deck()
for d in my_deck:
    print(d)

# doing above method instead of
# for d in my_deck.cards



















