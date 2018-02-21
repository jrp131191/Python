# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:53:06 2018

@author: James
"""

import random

class Card(object):
    """Represents a standard playing card."""  
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ['None', "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""      
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])


class Deck(object):
    """Represents a deck of cards.""" 
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
        """Removes and returns a card from the deck."""
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand."""
        for i in range(num):
            hand.add_card(self.pop_card())         
           
class Hand(Deck):
    """Represents a hand of playing cards."""    
    card = ''
    def __init__(self, label=''):
        self.cards = []
        self.rank = ''
        self.splits = []
        self.label = label
        self.score = 0
        self.scores = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'Jack': 10,'Queen': 10,'King': 10}
        
    def move_cards_split(self, hand2, num):
        for i in range(num):
            hand2.add_card(self.pop_card())
    
    def split(self, split_active = False):
        self.split_active = split_active
        sinp = None
        
        for card in self.cards:
            
            self.splits.append((str(card).splitlines()[0]).split(' ',1)[0])
        if self.splits[0] == self.splits[1]:
            self.split_active = True
            while sinp not in ['y','n']:
                sinp = input('Would you like to split? Please type \'y\' or \'n\': ')
                if sinp not in ['y','n']:
                    print('Error! Please enter a valid response. Type \'y\' or \'n\': ')
                else:
                    hand.move_cards_split(hand2,1)
                    break  
            

    
    def update_score(self):
        
        for card in self.cards:

            ainp = 0
            if 'Ace' in str(card):                
                while ainp not in [1,11]:
                    #ainp = int(input('You have an Ace. Would you like to set it\'s value to 1 or 11?: '))
                    ainp = 1
                    if ainp not in [1,11]:
                        print('Error! Ace can only take on the values 1 and 11! Please enter 1 or 11: ')
                    continue               
                self.score+= ainp                       
                continue
            if any(x in str(card) for x in Card.rank_names[11:]):
                self.score+= self.scores[(str(card).splitlines()[0]).split(' ',1)[0]]
            else:
                self.score += self.scores[(str(card).splitlines()[0]).split(' ',1)[0]]        
        if hand.split_active == True:
            print('Your current score for hand 1 is: ', self.score)
        else:
            print('Your current score is: ', self.score)
            
    def blackjack(self):
        if hand.score == 21:
            print('Blackjack!')
            
    def bust(self):
        if hand.score > 21:
            print('Bust!')
        
class Hand2(Hand):
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.score = 0
        self.scores = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'Jack': 10,'Queen': 10,'King': 10}
        
class Handai(Deck):
    """Represents a hand of playing cards for the AI."""    
    def __init__(self, label=''):
        self.cards = []
        self.label = label
        
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
    hand2 = Hand2()
    handai = Handai()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 2)
    deck.move_cards(handai, 2)

    #hand.sort()
    print('Player has:\n ', hand)
    
    print('Computer has:\n ', handai)
    hand.split()

    if hand.split_active == True:
        hand.update_score()
        hand2.update_score()
        print('Would you like to hit hand 1?: ')
        
    hand.update_score()
    
    hand.blackjack()
    hand.bust()
    
    while hand.score<21:
        hit = ""
        
        while hit not in ['y','n']:
            hit = input('Would you like to hit? Please type \'y\' or \'n\': ')
            if hit not in ['y','n']:
                print('Error! Please enter a valid response. Type \'y\' or \'n\': ')
            
            if hit is 'n':
                print('Standing on: ', hand.score)
                
            else:
                deck.move_cards(hand,1)
                
                hand.score = 0
                print('Drew a: ',str(hand))
                hand.update_score()
                
                hand.blackjack()
                hand.bust()
        break
        
        