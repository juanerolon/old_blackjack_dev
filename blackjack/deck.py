#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:55:45 2019

@author: Juan E Rolon
       : rolon.math@gmail.com
"""

import random

   
class Deck:
    
    def __init__(self):
    
        self.__cardIndex = []
        self.__counter = 0
        self.__drawnCards = []
        self.__cards = {}
        
        self.__n=0
        
        #this creates only a set of 52 integer indexes stored in a list
        while self.__n < 52:
            self.__cardIndex.append(self.__n+1)
            self.__n+=1
        
        #shuffle the index list
        random.shuffle(self.__cardIndex)
        
        self.create_deck()

    def create_deck(self):
      
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
        self.create_deck()