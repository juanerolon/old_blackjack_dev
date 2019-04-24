
""" creates geometrical figures using dieview class"""

from random import randrange
from graphics import GraphWin, Point

from button import Button
from dieview2 import DieView2 

def main():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 19, 19)
    win.setBackground("gray")

    # Draw the interface widgets


    die1 = DieView2(win, Point(3,7), 4,"blue","yellow")
      
    die2 = DieView2(win, Point(7,7), 2,"blue","yellow")
    
    die3 = DieView2(win, Point(11,7), 4,"red","yellow")
    
    die4 = DieView2(win, Point(7,11), 4,"red","yellow")
    
    die5 = DieView2(win, Point(7,3), 4,"red","yellow")
    
    
    rollButtonBlues = Button(win, Point(15,17), 7, 2, "Roll Blues")
    rollButtonBlues.activate()
    
    rollButtonReds = Button(win, Point(15,15), 7, 2, "Roll Reds")
    rollButtonReds.activate()
    
    
    quitButton = Button(win, Point(15,12), 3, 2, "Quit")
    quitButton.activate()

    # Event loop
    pt = win.getMouse()
    
    while not quitButton.clicked(pt):
        
        if rollButtonBlues.clicked(pt):
            
            value1 = randrange(1,7)
            die1.setValue(value1)

            value2 = randrange(1,7)
            die2.setValue(value2)
            
        if rollButtonReds.clicked(pt):
            
            value3 = randrange(1,7)
            die3.setValue(value3)
            
            value4 = randrange(1,7)
            die4.setValue(value4)
            
            value5 = randrange(1,7)
            die5.setValue(value5)
            
        pt = win.getMouse()

    # close up shop
    win.close()

main()
