#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:34:30 2019

@author: juanerolon


"""

import sys
import random

#----------------------------- classes ----------------------------------------
   
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
        
        
class Bet:
    
    def __init__(self):
        
        self.balance = 500
        self.status = True
                
    def make_bet(self,amount):
        self.balance = self.balance - amount

    def can_bet(self,amount):
        if (amount > self.balance and self.balance > 0):
            self.status = False
            return False
        else:
            self.status = True
            return True




class Dealer:
    
    def __init__(self):
        
        self.hand_value = 0
        self.hand = []
        self.hand_ct = 0
        self.aces_ct =0
        self.ace_flag = False
               
    def update_hand(self, card):
        
        if card[2] == 11:
            self.ace_flag = True
            self.aces_ct +=1
            
        self.hand.append(card)
        self.hand_value = self.hand_value + self.hand[self.hand_ct][2]
        
        if self.hand_value > 21 and self.ace_flag:
            self.hand_value = self.hand_value - 10
            print("Dealer got soft hand")
            
        self.hand_ct +=1
        
    def show_init_hand_value(self):
        return self.hand[random.choice([0,1])][2]
        
    def clear_hand(self):
        del self.hand[:]
        self.hand_value = 0
        self.hand_ct = 0
        self.aces_ct = 0
        self.ace_flag = False
        
    def can_hit(self):
        """Controls when dealer should stand"""
        if self.hand_value < 17:
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
        self.aces_ct = 0
        self.ace_flag = False
        self.__sysbet = Bet()
        
    
    def can_bet(self,amount):
        return self.__sysbet.can_bet(amount)
    
    def make_bet(self,amount):
        self.__sysbet.make_bet(amount)
        
    def get_balance(self):
        return self.__sysbet.balance

    def blnc_up_won(self,upamt):
        self.__sysbet.balance += upamt
        
    
    def update_hand(self, card):
        
        if card[2] == 11:
            self.ace_flag = True
            self.aces_ct +=1
        
        self.hand.append(card)
        self.hand_value = self.hand_value + self.hand[self.hand_ct][2]
                
        if self.hand_value > 21 and self.ace_flag:
            self.hand_value = self.hand_value - 10
            self.ace_flag = False
            print("Player got a soft hand")
            
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
        self.aces_ct = 0
        self.ace_flag = False
        


class Blackjack():
    
    def __init__(self):
        
        self.gD = Deck()
        self.P1 = Player()
        self.Dl = Dealer()
        
        self.roundFlag = True
        self.bamt = 0
        
        self.pwins_ct = 0
        self.ngmes_ct = 0
        
    
    #--X--
    
    def make_bets(self):
        
        flag = True
        while flag:
            self.bamt = 0
            if self.P1.can_bet(self.bamt):
                ans = input("Make bet (Y/N)?")
                if ans.strip().lower() == "y":
                    flag = False
                    self.bamt = eval(input("Enter amount:"))
                    self.P1.make_bet(self.bamt)
                elif ans.strip().lower() == "n":
                    ans2 = input("Stop game (Y/N)?")
                    if ans2.strip().lower() == "y":
                        self.roundFlag = False
                        break
                    elif ans2.strip().lower() == "n":
                        continue
                    else:
                        continue
                else:
                    continue
            else:
                flag = False
                
                
    #--X--
    
    def deal(self):
        
        flag = True
        while flag:
            
            ans = input("Deal (Y/N)?")
            if ans.strip().lower() == "y":
                flag = False
                self.Dl.update_hand(self.gD.draw_card())
                self.Dl.update_hand(self.gD.draw_card())
                self.P1.update_hand(self.gD.draw_card())
                self.P1.update_hand(self.gD.draw_card())
                print("Dealer hand: {}".format(self.Dl.hand))
                print("Dealer shown hand value: {}".format(self.Dl.show_init_hand_value()))
                print("Dealer actual hand value: {}".format(self.Dl.hand_value))
                print("Dealer can hit?: {}".format(self.Dl.can_hit()))
                print("Player hand: {}".format(self.P1.hand))
                print("Player hand value: {}".format(self.P1.hand_value))
                if self.P1.blackjack():
                    print("Player gets blackjack! Player wins!")               
                    self.roundFlag=False
                    self.pwins +=1
                    self.ngmes_ct +=1
                    self.P1.blnc_up_won(2.0 * self.bamt)
                    break
            elif ans.strip().lower() == "n":
                ans2 = input("Stop game (Y/N)?")
                if ans2.strip().lower() == "y":
                    self.P1.blnc_up_won(self.bamt)
                    self.roundFlag = False
                    break
                elif ans2.strip().lower() == "n":
                    continue
                else:
                    continue
            else:
                continue
            
    #--X--
            
    def main_loop(self):
        flag = True
        fflo = True
        while flag:
            ans = input("Hit (Y/N)?")
            if ans.strip().lower() == "y":
                self.P1.update_hand(self.gD.draw_card())
                print("Player hand: {}".format(self.P1.hand))
                print("Player hand value: {}".format(self.P1.hand_value))
                print("Player blackjack?: {}".format(self.P1.blackjack()))
                print("Player busted?: {}".format(self.P1.busted()))
                if self.P1.busted():
                    print("Player busted! Player Loss!")
                    flag = False
                    self.roundFlag = False
                    self.ngmes_ct +=1
                    break
                elif self.P1.blackjack():
                    print("Player gets blackjack! Player wins!")
                    self.P1.blnc_up_won(2.0 * self.bamt)
                    flag = False
                    self.roundFlag = False
                    self.pwins_ct +=1
                    self.ngmes_ct +=1
                    break            
                else:
                    pass
                    
            elif ans.strip().lower() == "n":
                flag = False
                while fflo:
                    if self.Dl.blackjack():
                        fflo = False
                        print("Dealer gets Blackjack! Player Loss!")
                        self.roundFlag = False
                        self.ngmes_ct +=1
                        break
                        
                    elif self.Dl.busted():
                        fflo = False
                        self.roundFlag = False
                        print("Dealer Busted! Player Wins!")
                        self.P1.blnc_up_won(2.0 * self.bamt)
                        self.pwins +=1
                        self.ngmes_ct +=1
                        break
                    elif self.Dl.can_hit():
                        self.Dl.update_hand(self.gD.draw_card())
                        print("Dealer hand: {}".format(self.Dl.hand))
                        print("Dealer actual hand value: {}".format(self.Dl.hand_value))
                        print("Dealer can hit?: {}".format(self.Dl.can_hit()))
                        
                        if self.Dl.blackjack():
                            fflo = False
                            flag = False
                            self.roundFlag = False
                            print("Dealer gets Blackjack! Player Loss!")
                            self.ngmes_ct +=1
                            break
                        
                        if self.Dl.busted():
                            fflo = False
                            flag = False
                            self.roundFlag = False
                            print("Dealer Busted! Player Wins!")
                            self.P1.blnc_up_won(2.0 * self.bamt)
                            self.pwins +=1
                            self.ngmes_ct +=1
                            break
                            
                        if  self.Dl.hand_value > self.P1.hand_value:
                            print("Dealer has greater hand value! Player Loss!")
                            fflo = False
                            flag = False
                            self.roundFlag = False
                            self.ngmes_ct +=1
                            break                       
                    elif self.P1.hand_value > self.Dl.hand_value:
                        print("Player has greater hand value! Player Wins!")
                        self.P1.blnc_up_won(2.0 * self.bamt)
                        fflo = False
                        flag = False
                        self.roundFlag = False
                        self.pwins +=1
                        self.ngmes_ct +=1
                        break
                    elif self.Dl.hand_value > self.P1.hand_value:
                        print("Dealer has greater hand value! Player Loss!")
                        fflo = False
                        flag = False
                        self.roundFlag = False
                        self.ngmes_ct +=1
                        break
                    elif self.Dl.hand_value == self.P1.hand_value:
                        print("Push! Tied round!")
                        self.P1.blnc_up_won(self.bamt)
                        fflo = False
                        flag = False
                        self.roundFlag = False
                        self.ngmes_ct +=1
                        break                        
                    else:
                        print("Unknown condition")
                        self.ngmes_ct +=1
                        break
            else:
                break
       


                    
if __name__ == "__main__":  
    
   bgame = Blackjack()
   
   while bgame.roundFlag:
   
       if bgame.roundFlag: print("Player balance: {}".format(bgame.P1.get_balance()))
       if bgame.roundFlag: bgame.make_bets()
       
       if bgame.roundFlag: bgame.deal()
       if bgame.roundFlag: bgame.main_loop()
       
       if bgame.roundFlag: 
           ans = input("\n\n Play another round? (Y/N)?")
           if ans.strip().lower() == "y":
               keep_play = True
               bgame.roundFlag = True
               bgame.P1.clear_hand()
               bgame.Dl.clear_hand()
               bgame.gD.shuffle()                         
           elif ans.strip().lower() == "n":
                bgame.roundFlag = False
           else:
                continue
            
       
   
   print("\n\nPlayer end balance\n\n: {}".format(bgame.P1.get_balance())) 
   print("\n\nGame stats:\n\n") 
   print("Number of rounds played : {}".format(bgame.ngmes_ct))
   print("Number of wins by player: {}".format(bgame.pwins_ct))

    
    

    
    
    
   
    
    
    
    
    
    
  
        
        
    
  
    
    

       

