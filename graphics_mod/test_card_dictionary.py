#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:34:30 2019

@author: juanerolon


"""

import random


def test_deck():

    deck = {}
    
    #clubs
    
    deck[1] = ["Ace", "Ace of Clubs", 11]
    deck[2] = ["2", "Two of Clubs",2]
    deck[3] = ["3", "Three of Clubs",3]
    deck[4] = ["4", "Four of Clubs",4]
    deck[5] = ["5", "Five of Clubs",5]
    deck[6] = ["6", "Six of Clubs",6]
    deck[7] = ["7", "Seven of Clubs",7]
    deck[8] = ["8", "Eight of Clubs",8]
    deck[9] = ["9", "Nine of Clubs",9]
    deck[10] = ["10", "Ten of Clubs",10]
    deck[11] = ["Jack", "Jack of Clubs",10]
    deck[12] = ["King", "King of Clubs",10]
    deck[13] = ["Queen", "Queen of Clubs",10]
    
    #diamonds
    
    deck[14] = ["Ace", "Ace of Diamonds", 11]
    deck[15] = ["2", "Two of Diamonds",2]
    deck[16] = ["3", "Three of Diamonds",3]
    deck[17] = ["4", "Four of Diamonds",4]
    deck[18] = ["5", "Five of Diamonds",5]
    deck[19] = ["6", "Six of Diamonds",6]
    deck[20] = ["7", "Seven of Diamonds",7]
    deck[21] = ["8", "Eight of Diamonds",8]
    deck[22] = ["9", "Nine of Diamonds",9]
    deck[23] = ["10", "Ten of Diamonds",10]
    deck[24] = ["Jack", "Jack of Diamonds",10]
    deck[25] = ["King", "King of Diamonds",10]
    deck[26] = ["Queen", "Queen of Diamonds",10]
    
    
    #hearts
    
    deck[27] = ["Ace", "Ace of Hearts", 11]
    deck[28] = ["2", "Two of Hearts",2]
    deck[29] = ["3", "Three of Hearts",3]
    deck[30] = ["4", "Four of Hearts",4]
    deck[31] = ["5", "Five of Hearts",5]
    deck[32] = ["6", "Six of Hearts",6]
    deck[33] = ["7", "Seven of Hearts",7]
    deck[34] = ["8", "Eight of Hearts",8]
    deck[35] = ["9", "Nine of Hearts",9]
    deck[36] = ["10", "Ten of Hearts",10]
    deck[37] = ["Jack", "Jack of Hearts",10]
    deck[38] = ["King", "King of Hearts",10]
    deck[39] = ["Queen", "Queen of Hearts",10]
    
    
    #spades
    
    deck[40] = ["Ace", "Ace of Spades", 11]
    deck[41] = ["2", "Two of Spades",2]
    deck[42] = ["3", "Three of Spades",3]
    deck[43] = ["4", "Four of Spades",4]
    deck[44] = ["5", "Five of Spades",5]
    deck[45] = ["6", "Six of Spades",6]
    deck[46] = ["7", "Seven of Spades",7]
    deck[47] = ["8", "Eight of Spades",8]
    deck[48] = ["9", "Nine of Spades",9]
    deck[49] = ["10", "Ten of Spades",10]
    deck[50] = ["Jack", "Jack of Spades",10]
    deck[51] = ["King", "King of Spades",10]
    deck[52] = ["Queen", "Queen of Spades",10]
    
    
    #draw 20 cards
    
    print("\n\n")
    print("Deck size: {}\n".format(len(deck)))
    
    ct = 0
    while ct < 2:
        rancard = random.randrange(1,52)
        print(deck[rancard])
        del deck[rancard]
        ct +=1
        
    print("\n")
    print("Remaining deck size: {}\n".format(len(deck)))
    
    
    
    
class Deck:
    
    def __init__(self):
    
        self.__cardIndex = []
        self.__counter = 0
        self.__drawnCards = []
        self.__cards = {}
        
        self.__n=0
        
        while self.__n < 52:
            self.__cardIndex.append(self.__n+1)
            self.__n+=1
            
        random.shuffle(self.__cardIndex)
        #print(self.__cardIndex)
    
        
        self.__cards[1] = ["Ace", "Ace of Clubs", 11]
        self.__cards[2] = ["2", "Two of Clubs",2]
        self.__cards[3] = ["3", "Three of Clubs",3]
        self.__cards[4] = ["4", "Four of Clubs",4]
        self.__cards[5] = ["5", "Five of Clubs",5]
        self.__cards[6] = ["6", "Six of Clubs",6]
        self.__cards[7] = ["7", "Seven of Clubs",7]
        self.__cards[8] = ["8", "Eight of Clubs",8]
        self.__cards[9] = ["9", "Nine of Clubs",9]
        self.__cards[10] = ["10", "Ten of Clubs",10]
        self.__cards[11] = ["Jack", "Jack of Clubs",10]
        self.__cards[12] = ["King", "King of Clubs",10]
        self.__cards[13] = ["Queen", "Queen of Clubs",10]
        
        #diamonds
        
        self.__cards[14] = ["Ace", "Ace of Diamonds", 11]
        self.__cards[15] = ["2", "Two of Diamonds",2]
        self.__cards[16] = ["3", "Three of Diamonds",3]
        self.__cards[17] = ["4", "Four of Diamonds",4]
        self.__cards[18] = ["5", "Five of Diamonds",5]
        self.__cards[19] = ["6", "Six of Diamonds",6]
        self.__cards[20] = ["7", "Seven of Diamonds",7]
        self.__cards[21] = ["8", "Eight of Diamonds",8]
        self.__cards[22] = ["9", "Nine of Diamonds",9]
        self.__cards[23] = ["10", "Ten of Diamonds",10]
        self.__cards[24] = ["Jack", "Jack of Diamonds",10]
        self.__cards[25] = ["King", "King of Diamonds",10]
        self.__cards[26] = ["Queen", "Queen of Diamonds",10]
        
        
        #hearts
        
        self.__cards[27] = ["Ace", "Ace of Hearts", 11]
        self.__cards[28] = ["2", "Two of Hearts",2]
        self.__cards[29] = ["3", "Three of Hearts",3]
        self.__cards[30] = ["4", "Four of Hearts",4]
        self.__cards[31] = ["5", "Five of Hearts",5]
        self.__cards[32] = ["6", "Six of Hearts",6]
        self.__cards[33] = ["7", "Seven of Hearts",7]
        self.__cards[34] = ["8", "Eight of Hearts",8]
        self.__cards[35] = ["9", "Nine of Hearts",9]
        self.__cards[36] = ["10", "Ten of Hearts",10]
        self.__cards[37] = ["Jack", "Jack of Hearts",10]
        self.__cards[38] = ["King", "King of Hearts",10]
        self.__cards[39] = ["Queen", "Queen of Hearts",10]
        
        
        #spades
        
        self.__cards[40] = ["Ace", "Ace of Spades", 11]
        self.__cards[41] = ["2", "Two of Spades",2]
        self.__cards[42] = ["3", "Three of Spades",3]
        self.__cards[43] = ["4", "Four of Spades",4]
        self.__cards[44] = ["5", "Five of Spades",5]
        self.__cards[45] = ["6", "Six of Spades",6]
        self.__cards[46] = ["7", "Seven of Spades",7]
        self.__cards[47] = ["8", "Eight of Spades",8]
        self.__cards[48] = ["9", "Nine of Spades",9]
        self.__cards[49] = ["10", "Ten of Spades",10]
        self.__cards[50] = ["Jack", "Jack of Spades",10]
        self.__cards[51] = ["King", "King of Spades",10]
        self.__cards[52] = ["Queen", "Queen of Spades",10]
        
    def draw_card(self):
        num = self.__cardIndex[self.__counter]
        card = self.__cards[num]
        del self.__cards[num]
        self.__counter +=1
        return card
    
    def getCards_count(self):
        return len(self.__cards)
    
    def shuffle(self):
        self.__counter = 0
        random.shuffle(self.__cardIndex)
        
        
def testDeck():
    
    myDeck = Deck()
    print(myDeck.getCards_count())

    card = myDeck.draw_card()
    print(card)
    for el in card:
        print(el)
    print(myDeck.getCards_count())

    card = myDeck.draw_card()
    print(card)
    for el in card:
        print(el)
    print(myDeck.getCards_count())
    
    card = myDeck.draw_card()
    print(card)
    for el in card:
        print(el)
    print(myDeck.getCards_count())
          
    
class Bet:
    
    def __init__(self):
        
        self.balance = 500
        self.status = True
                
    def make_bet(self,amount):
        if (amount > self.balance and self.balance > 0):
            self.status = False
        else:
            self.balance = self.balance - amount

def testBet():
            
    p1b = Bet()
    p1b.make_bet(100)
    print(p1b.balance)
    p1b.make_bet(650)
    print(p1b.balance)
    print(p1b.status)



class Dealer:
    
    def __init__(self):
        
        self.hand_value = 0
        self.hand = []
        self.hand_ct = 0
        
    def update_hand(self, card):
        self.hand.append(card)
        self.hand_value = self.hand_value + self.hand[self.hand_ct][2]
        self.hand_ct +=1
        
    def clear_hand(self):
        del self.hand[:]
        self.hand_value = 0
        self.hand_ct = 0
        
    def action_hit(self):
        if self.hand_value < 15:
            return True
        else:
            return False
        
    def blackjack(self):
        if self.hand_value == 21:
            return True
        else:
            return False
        
    def busted(self):
        if self.hand_value > 21:
            return True
        else:
            return False
        
class Player:
    
    def __init__(self):
        
        self.hand_value = 0
        self.hand = []
        self.hand_ct = 0
        self.bet = Bet()
        
    def update_hand(self, card):
        self.hand.append(card)
        self.hand_value = self.hand_value + self.hand[self.hand_ct][2]
        self.hand_ct +=1
        
    def blackjack(self):
        if self.hand_value == 21:
            return True
        else:
            return False
        
    def busted(self):
        if self.hand_value > 21:
            return True
        else:
            return False
        
    def clear_hand(self):
        del self.hand[:]
        self.hand_value = 0
        self.hand_ct = 0
        
        
        
    
        
if __name__ == "__main__":
    
    P1 = Player()
    Dl = Dealer()
    
    gameDeck = Deck()
    
  
    if False:
    
        Dl.update_hand(gameDeck.draw_card())
        Dl.update_hand(gameDeck.draw_card())
        
        print(Dl.hand)
        print(Dl.hand_value)
        Dl.clear_hand()
        print(Dl.hand)
        print(Dl.hand_value)
    
    
    print("\nDealer:\n")
    
    Dl.update_hand(gameDeck.draw_card())
    Dl.update_hand(gameDeck.draw_card())
    
    print(Dl.hand)
    print("Dealer hand value: {}".format(Dl.hand_value))
    print("Dealer action hit?: {}".format(Dl.action_hit()))
    print("Dealer blackjack?: {}".format(Dl.blackjack()))
    print("Dealer busted?: {}".format(Dl.busted()))
    
    print("\nPlayer:\n")
    
    P1.update_hand(gameDeck.draw_card())
    P1.update_hand(gameDeck.draw_card())
    print(P1.hand)
    print("Player hand value: {}".format(P1.hand_value))
    print("Player blackjack?: {}".format(P1.blackjack()))
    print("Player busted?: {}".format(P1.busted()))
    
    
    print(gameDeck.getCards_count())
    
    
    
    
  
        
        
    
  
    
    

       


