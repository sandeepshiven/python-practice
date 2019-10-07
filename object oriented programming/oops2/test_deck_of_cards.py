import unittest
from deck2 import Card,Deck


class test_Card(unittest.TestCase):
    def setUp(self):
        self.card = Card('Hearts','A')

    def test__init(self):
        ''' Eack card should have a suit and value'''
        self.assertEqual(self.card.suit,'Hearts')
        self.assertEqual(self.card.value,'A')
    
    def test_repr(self):
        """ Representation should be 'Value of Suit' """
        self.assertEqual(repr(self.card),"A of Hearts")

class test_Deck(unittest.TestCase):
    
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """ There Should be 52 cards """
        self.assertTrue(isinstance(self.deck.cards,list))
        self.assertEqual(len(self.deck.cards), 52)
        self.assertEqual(self.deck.no_of_cards,52)

    def test_count(self):
        """ Count should return no. of cards """
        self.deck.deal_card()
        self.assertEqual(self.deck.count(),len(self.deck.cards))

    def test_repr(self):
        """ Repsentation Should be 'Deck of {no of cards} cards """
        self.deck.deal_card()
        self.deck.deal_card()
        self.assertEqual(repr(self.deck),"Deck of 50 cards")

    def test_deal(self):
        """ Deal should return no. of cards we dealt """
        self.assertEqual(len(self.deck._deal(5)),5)
        self.assertEqual(len(self.deck._deal(47)),47)
       
        with self.assertRaises(ValueError):
            self.deck._deal(5)
        
    def test_shuffle(self):
        """ Shuffle should shuffle and return 52 cards """
        self.deck.shuffle()
        self.assertEqual(len(self.deck.cards),52)
       
        with self.assertRaises(ValueError):
            self.deck.deal_card()
            self.deck.shuffle()

    def test_deal_card(self):
        """ Deal card should return only 1 card """
        #print(type(self.deck.deal_card()))
        self.assertTrue(isinstance(self.deck.deal_card(),Card))        

    def test_deal_hand(self):
        """ Deal hand should return desired no of cards """
        self.assertEqual(len(self.deck.deal_hand(5)), 5)
        with self.assertRaises(ValueError):
            self.deck.deal_hand(47)
            self.deck.deal_hand(21)




if __name__ == '__main__':
    unittest.main()

