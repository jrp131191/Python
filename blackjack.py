# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:53:06 2018

@author: James
"""

import random

class Card(object):
    """Represents a standard playing card.
    
    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """
    
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ['None', "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])


class Deck(object):
    """Represents a deck of cards.
    
    Attributes:
      cards: list of Card objects.
    """
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck."""
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())
            
class Hand(Deck):
    """Represents a hand of playing cards."""
    scores = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'Jack': 10,'Queen': 10,'King': 10}    

    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.score = 0
        
    def update_score(self):
        
        for card in self.cards:
            ainp = 0
            if 'Ace' in str(card):                
                while ainp not in [1,11]:
                    ainp = int(input('You have an Ace. Would you like to set it\'s value to 1 or 11?: '))
                    if ainp not in [1,11]:
                        print('Error! Ace can only take on the values 1 and 11! Please enter 1 or 11: ')
                    continue               
                self.score+= ainp                       
                continue
            if any(x in str(card) for x in Card.rank_names[11:]):
                self.score+= Hand.scores[str(card).split(" ")[0]]
            else:
                self.score += Hand.scores[str([int(s) for s in str(card).split() if s.isdigit()][0])]
        print('Your current score is: ', self.score)
        
class Handai(Deck):
    """Represents a hand of playing cards for the AI."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label
        
#class Score():
#    
#    scores = ['none', 1, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#    
#    def __init__(self, score=[0,0]):
#        self.score = score
#        
    #def add_score(self):       
        #self.score = [Score.scores[Hand.cardval], Score.scores[Card.rank_names.index(Handai.handai[0])]]
        
        #.index(" ..")

def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    handai = Handai()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 2)
    deck.move_cards(handai, 2)

    #hand.sort()
    print('Player has:\n ', hand)
    
    print('Computer has:\n ', handai)
    
    hand.update_score()
    