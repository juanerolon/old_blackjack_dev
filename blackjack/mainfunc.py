#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:05:00 2019

@author: juanerolon
"""

import os
from gameplay import Blackjack


if __name__ == "__main__":
    
   os.system("clear") 
    
   bgame = Blackjack()
   
   while bgame.gameFlag:
           
       print("Your balance is : {}".format(bgame.P1.get_balance())) 
        
       bgame.make_bets()
                
       if bgame.gameFlag : bgame.deal()
       if bgame.roundFlag : bgame.main_loop()
       
       if bgame.gameFlag and bgame.P1.get_balance() > 0: 
           ans = input("\n\n Play another round? (Y/N)?")
           if ans.strip().lower() == "y":
               bgame.roundFlag = True
               bgame.P1.clear_hand()
               bgame.Dl.clear_hand()
               bgame.gD.shuffle()                         
           elif ans.strip().lower() == "n":
                bgame.gameFlag = False
           else:
                continue
            
       
   
   print("\nPlayer end balance: {}\n".format(bgame.P1.get_balance())) 
   print("\nGame stats:\n") 
   print("Number of rounds played : {}".format(bgame.ngmes_ct))
   print("Number of wins by player: {}".format(bgame.pwins_ct))