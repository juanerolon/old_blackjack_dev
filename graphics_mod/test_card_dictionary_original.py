#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:38:46 2019

@author: juanerolon
"""

import random


class Aox:
    
    def __init__(self,x):
        
        self.x = x
        
    def isgfive(self):
        
        return self.x > 5
    
    def cond(self):
        if self.isgfive():
            print(" x > 5")
            
    def printa(self):
        
        print(self.x)
            

            
def test2():
    
    a = Aox(6)
    
    a.cond()
    a.printa()
    
    

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
    
if __name__ == "__main__":
    
    test2()
    