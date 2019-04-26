#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:12:48 2019

@author: juanerolon
"""

#-------------------- game functions ----------------------
        
#----------------- misc test functions --------------------

from test_modular_blackjack_game import * 
        
def testBet():
            
    p1b = Bet()
    p1b.make_bet(100)
    print(p1b.balance)
    p1b.make_bet(650)
    print(p1b.balance)
    print(p1b.status)
    
    
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
    

def test_clearing_hand():

    Dl.update_hand(gameDeck.draw_card())
    Dl.update_hand(gameDeck.draw_card())
    
    print(Dl.hand)
    print(Dl.hand_value)
    Dl.clear_hand()
    print(Dl.hand)
    print(Dl.hand_value)
    
def test_initial_game_stage():
    P1 = Player()
    Dl = Dealer()
    
    gameDeck = Deck()
       
    print("\nDealer:\n")
    
    Dl.update_hand(gameDeck.draw_card())
    Dl.update_hand(gameDeck.draw_card())
    
    
    print(Dl.hand)
    print("Dealer hand value: {}".format(Dl.hand_value))
    print("Dealer shown hand value: {}".format(Dl.show_init_hand_value()))
    print("Dealer action hit?: {}".format(Dl.can_hit()))
    print("Dealer blackjack?: {}".format(Dl.blackjack()))
    print("Dealer busted?: {}".format(Dl.busted()))
    
    print("\nPlayer:\n")
    
    print("Player initial balance: {}".format(P1.get_balance()))
    bamt = 150
    print("Is the player able to put a bet of ${}?: {}".format(bamt, P1.can_bet(bamt)))
    if P1.can_bet(bamt):
        P1.make_bet(bamt)
    print("Player current balance: {}".format(P1.get_balance()))
    
    P1.update_hand(gameDeck.draw_card())
    P1.update_hand(gameDeck.draw_card())
    print(P1.hand)
    print("Player hand value: {}".format(P1.hand_value))
    print("Player blackjack?: {}".format(P1.blackjack()))
    print("Player busted?: {}".format(P1.busted()))
    
    
    print(gameDeck.getCards_count())
    
    #----------------- game play tests ---------------------------------------

def game_play_test1():
          
    gD = Deck()
    P1 = Player()
    Dl = Dealer()
    
    gameFlag = True
    
        
    flag = True
    while flag:
        bamt = 0
        if P1.can_bet(bamt):
            ans = input("Make bet (Y/N)?")
            if ans.strip().lower() == "y":
                flag = False
                bamt = eval(input("Enter amount:"))
                P1.make_bet(bamt)
            elif ans.strip().lower() == "n":
                ans2 = input("Stop game (Y/N)?")
                if ans2.strip().lower() == "y":
                    gameFlag = False
                    break
                elif ans2.strip().lower() == "n":
                    continue
                else:
                    continue
            else:
                continue
        else:
            flag = False
        
    
    print("Player current balance: {}".format(P1.get_balance()))
    
    flag = True
    while flag:
        
        ans = input("Deal (Y/N)?")
        if ans.strip().lower() == "y":
            flag = False
            Dl.update_hand(gD.draw_card())
            Dl.update_hand(gD.draw_card())
            P1.update_hand(gD.draw_card())
            P1.update_hand(gD.draw_card())
            print("Dealer hand: {}".format(Dl.hand))
            print("Dealer shown hand value: {}".format(Dl.show_init_hand_value()))
            print("Dealer actual hand value: {}".format(Dl.hand_value))
            print("Dealer can hit?: {}".format(Dl.can_hit()))
            print("Player hand: {}".format(P1.hand))
            print("Player hand value: {}".format(P1.hand_value))
            if P1.blackjack():
                print("Player gets blackjack! Player wins!")               
                gameFlag=False
                break
        elif ans.strip().lower() == "n":
            ans2 = input("Stop game (Y/N)?")
            if ans2.strip().lower() == "y":
                gameFlag = False
                break
            elif ans2.strip().lower() == "n":
                continue
            else:
                continue
        else:
            continue
    
    #say no below when players gets blackjack from the start... need to move below
    #code into above    
        
    flag = True
    fflo = True
    while flag:
        ans = input("Hit (Y/N)?")
        if ans.strip().lower() == "y":
            P1.update_hand(gD.draw_card())
            print("Player hand: {}".format(P1.hand))
            print("Player hand value: {}".format(P1.hand_value))
            print("Player blackjack?: {}".format(P1.blackjack()))
            print("Player busted?: {}".format(P1.busted()))
            if P1.busted():
                print("Player busted! Player Loss!")
                flag = False
                break
            elif P1.blackjack():
                print("Player gets blackjack! Player wins!")
                flag = False
                gameFlag = False
                break            
            else:
                pass
                
        elif ans.strip().lower() == "n":
            flag = False
            while fflo:
                if Dl.blackjack():
                    fflo = False
                    print("Dealer gets Blackjack! Player Loss!")
                    break
                    
                elif Dl.busted():
                    fflo = False
                    print("Dealer Busted! Player Wins!")
                    break
                elif Dl.can_hit():
                    Dl.update_hand(gD.draw_card())
                    print("Dealer hand: {}".format(Dl.hand))
                    print("Dealer actual hand value: {}".format(Dl.hand_value))
                    print("Dealer can hit?: {}".format(Dl.can_hit()))
                    
                    if Dl.blackjack():
                        fflo = False
                        flag = False
                        print("Dealer gets Blackjack! Player Loss!")
                        break
                    
                    if Dl.busted():
                        fflo = False
                        flag = False
                        print("Dealer Busted! Player Wins!")
                        break
                        
                    if  Dl.hand_value > P1.hand_value:
                        print("Dealer has greater hand value! Player Loss!  -X-")
                        fflo = False
                        flag = False
                        break                       
                elif P1.hand_value > Dl.hand_value:
                    print("Player has greater hand value! Player Wins!")
                    fflo = False
                    flag = False
                    break
                elif Dl.hand_value > P1.hand_value:
                    print("Dealer has greater hand value! Player Loss!  -Y-")
                    fflo = False
                    flag = False
                    break
                elif Dl.hand_value == P1.hand_value:
                    print("Push! Tied round!")
                    fflo = False
                    flag = False
                    break
                    
                else:
                    print("Unknown condition")
                    break
        else:
            break