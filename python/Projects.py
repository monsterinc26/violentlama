# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 13:39:16 2020

@author: Ravi
"""


"""
Project number 1
Number guessing 

"""
import random
while 1:
    
    try:
        n=int(input("Enter a number "))
        
        if n==str(n):
            print("invalid input")
            
        if n>4:
            print("Enter value between 1 and 4")
            break
            
        t=random.choice([1,2,3,4])
        
        if n == t:
            print("You have guessed the number correctly")
            
        else:
            print("You lost!")
            
        z=input("Do you want to continue playing? ")
        if z=="no":
            break
    except ValueError as e:
        print("The error is", e)
    
"""
Project number 2
Dice rolling simulator

"""
import random
import time

while 1:
    
    roll=input("Press r to roll the dices ")
    if roll=="r":
        print("\nRolling the dices...")
        time.sleep(2)
    else:
        print("invalid input")
        
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    
    print("Dice 1=",dice1,"Dice 2=",dice2)
    
    if dice1==dice2:
        print("It's a double! ")
        
    else:
        print("Keep Trying")
        
    z=input("Do you want to keep trying? [Y/N]")
    if z=='n':
        break
    
"""
Project Number 3
Binary search algorithm

"""

def search(list,n):
    l=0
    u=len(list)
    
    while l<=u:
        mid=(l+u)//2
        
        if list[mid]==n:
            globals() ['pos']=mid
            return True
        else:
            if list[mid] < n:
                l=mid
                
            else:
                u=mid
                
p=[999,1000,987,500,4567,388]
p.sort()
n=987

if search(p,n):
    print("found at",pos)
else:
    print("not found")
     
"""
Linear search

"""


p=[999,1000,987,500,4567,388]
p.sort()
n=1000

if n in p:
    print("Found at",p.index(n))
    
else:
    print("not found")



























    
