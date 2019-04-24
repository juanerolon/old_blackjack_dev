#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:45:42 2019

@author: juanerolon
"""

def marx(f,N):
    return (f + 1) % N

class Test:
    def __init__(self,x,y):
   
        if (x < 0) or (y < 0):
            raise Exception(" x must be positive")
        else:
            print("A test object was instantiated")
            pass
        
        self._x = x
        self._y = y
        
    def boolMultiply(self):
        return self._x * self._y == 0
    
    def __innerTest__():
        print("Inner test")
        
    __innerTest__()
    
    
if __name__ == "__main__":

    myob = Test(1,1)
    print(myob.boolMultiply())
      
    foo = 5 > 3
    fuy = [1,2]
    
    print(foo.__bool__())
    print(fuy.__len__())
    
    
    print("\n ** marx: circular pattern N=3 **\n")
    
    N=3
    
    print(marx(1,N))
    print(marx(2,N))
    print(marx(3,N))
    print(marx(4,N))
    print(marx(5,N))
    print(marx(6,N))
    print(marx(7,N))
    
    print("\n ** marx: circular pattern N=4 **\n")
    
    N=4
       
    print(marx(1,N))
    print(marx(2,N))
    print(marx(3,N))
    print(marx(4,N))
    print(marx(5,N))
    print(marx(6,N))
    print(marx(7,N))
