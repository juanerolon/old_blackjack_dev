#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:55:19 2019

@author: juanerolon
"""

# imports all classes from graphics module (graphics.py)
from graphics import * 


def testImage4():
    win = GraphWin("Card", 300, 500)
    win.setCoords(0,0,300,500)
    
    #image 1
    cardImage = Image(Point(80,90), "ace_of_spades3.gif")
    cardImage.draw(win)
    
    win.getMouse()
    
    #image 2
    cardImage2 = Image(Point(110,90), "ace_of_spades3.gif")
    cardImage2.draw(win)
    
    win.getMouse()
    
    #image 3
    cardImage2 = Image(Point(140,90), "ace_of_spades3.gif")
    cardImage2.draw(win)
    
    win.getMouse()
    
    #image 4
    cardImage2 = Image(Point(80,400), "ace_of_spades3.gif")
    cardImage2.draw(win)
    
    win.getMouse()
    
    #image 5
    cardImage2 = Image(Point(110,400), "ace_of_spades3.gif")
    cardImage2.draw(win)
    
    win.getMouse()
    
    #image 6
    cardImage2 = Image(Point(140,400), "ace_of_spades3.gif")
    cardImage2.draw(win)
    
    

    
    win.getMouse()
    win.close()



def testImage3():
    win = GraphWin("Card", 300, 200)
    win.setCoords(0,0,125,180)
    
    #image 1
    cardImage = Image(Point(40,90), "ace_of_spades3.gif")
    cardImage.draw(win)
    
    win.getMouse()
    
    #image 2
    cardImage2 = Image(Point(60,90), "ace_of_spades3.gif")
    cardImage2.draw(win)
    
    win.getMouse()
    
    #image 3
    cardImage2 = Image(Point(80,90), "ace_of_spades3.gif")
    cardImage2.draw(win)
    
    

    
    win.getMouse()
    win.close()



def testImage2():
    win = GraphWin("Card", 150, 200)
    win.setCoords(0,0,125,180)
    cardImage = Image(Point(75,90), "ace_of_spades3.gif")
    cardImage.draw(win)
    
    
    #centerPoint = cardImage.getAnchor()
    widthInPixels = cardImage.getWidth()
    heightInPixels = cardImage.getHeight()
    
    #print(centerPoint)
    print(widthInPixels)
    print(heightInPixels)
    
    win.getMouse()
    win.close()



def testImage():
    win = GraphWin("Card", 600, 800)
    win.setCoords(0,0,500,726)
    
    #image 1
    cardImage = Image(Point(250,380), "ace_of_spades2.gif")
    cardImage.draw(win)
    
    
    #centerPoint = cardImage.getAnchor()
    widthInPixels = cardImage.getWidth()
    heightInPixels = cardImage.getHeight()
    
    #print(centerPoint)
    print(widthInPixels)
    print(heightInPixels)
    
    win.getMouse()
    win.close()




def testText():
    """Opens win object, displays text, waits for mouse click on window
    to terminate the application"""
    win = GraphWin()
    win.setCoords(0,0,10,10)
    t = Text(Point(5,5), "Centered Text")
    t.draw(win)
    win.getMouse()
    win.close()
    
    
if __name__ == "__main__":
    testImage4()




