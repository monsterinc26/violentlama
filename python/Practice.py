# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 21:02:51 2019

@author: Ravi
"""

z=input("Enter the string ")

lower=0
upper=0
alpha=0
num=0


for i in z:
    if i.islower():
        lower=lower+1
        
    
    if i.isupper():
        upper=upper+1
        
        
    if i.isalpha():
        alpha=alpha+1
        
    if i.isnumeric():
        num=num+1
        
        
        
        
print("The lower alphabets are",lower)
print("The upper alphabets are",upper)
print("The alphabets are",alpha)
print("The amount of digits are",num)
    

num=[1,2,3,4,5]

num_new=[i**2 for i in num]

def x (a):
    return a**2

nums=list(map(x,num))
print(nums)


a=["abc","abcd","abcde"]

for i in a:
    print(len(i))
    

print(len(a))

leng=list(map(len,a))

print(leng)

#Deposit and withdraw

Amount = 0



while 1:
    
    d=input("deposit or withdraw ")
    
    if d == "deposit" :
        y= int(input("Enter the deposit amount "))
        
        Amount=Amount+y
         
    else:
        z=int(input("enter the amount you want to withdraw "))
        
        Amount=Amount-z
        print("The net amount is",Amount)
        break

    
        
        
        
z=int(input("Facotrial of "))

n=1

for i in range(1,z+1):
    
    n=n*i
    
    print(n)
    
#Prime number
z=int(input("number "))

if z<=1:
    print("please enter valid input")


for i in range(2,z):
    if z % i==0:
           print("number is not prime")
           print(i,"times",z//i,"is",z)
           break
        
else:
       print("number is prime")
       
       
       
z=input("Enter yes or no ")

if z=="yes":
    print("yes")
    
else:
    print("no")
    


num=int(input("Enter the number"))

sum=0

while num > 0:
    d=num % 10
    num=num//10
    sum=sum+d
    print(num)
    break




for i in range(5):    
      
      for j in range (i):
         print("*",end="")
      print()

i=1

while i <=5:
    
    print("Hello",end="")
    
    i=i+1
    
    j=1
    
    while j <=5:
        
        print("Telusko",end="")
        j=j+1
        
    print()
        
        
i=1

for i in range(1,5):
    
    print("Hello",end="")
    
    for j in range(1,5):
        
        print("Telusko",end="")
        
print()
        
        


for i in range(4):
    
    for j in range(4):
        print("#",end="")
    
    print()
    
for i in range(4):
    
    for j in range(4-i):
        print("*",end="")
        
    print()

for i in range(5):
    for j in range(i+1):
        print("   *  ",end="")
        
    print()

    
#Assignment
    
 
num=int(input("enter a number "))

a=0

while num > 0:
    
    x=num % 10
    
    a=a+x
    
    num=int(num/10)  #or you can also use num=num//10) 
    
    print(a)
# for whole loop print, use print along the line of while
    
#Patterns
    
for x in range(5):
    
    for y in range(5):
         print("*",end="")
         
    print("*")

    
 #Assignment
       
z=input("enter a string ")
 
for i in z:
     print(i,"=",ord(i))
     
#Practice

x=int(input ("Enter the figure you want sum of "))

a=0

while x > 0:
    
    d = x % 10
    
    a = a + d
    
    x = x//10
    
print("The sum of figure is",a)
        

#Practice

up=0
right=0
down=0
left=0

while 1:
    
    z=input("Please mention in which direction you want to move ")
    d=int(input("And number of steps"))
    
    
    if z=="up":
        up=up+d
        print("up",up)
        
    if z=="down":
        down=down+d
        print("down",down)
        
    if z=="right":
        right=right+d
        print("right",right)
        
    if z=="left":
        left=left+d
        print("left",left)
        
    y=input("Do you want to quit")
    
    if y=="yes":
        break
    
    print("up",up,"down",down,"right",right,"left",left)
    
    
#pattern
    
for i in range(5):
    for j in range(i):
        print("*",end="")
        
    print()
    
a=0   
for i in range(5):
    
    for j in range(i+2):
        
        print("*",end="")
    print()
        
    
    
    
    
    
    
random.choice([1,2,5,8,7])
random.randrange(20,50,2)

#Stone paper scissors coding
import random
print('1= paper\n2= scissors\n3= stones')

while 1:

   z=int(input("enter the number "))
   
   if z!=3 and z!=2 and z!=1:
       print("invalid input")
       break

   if z==1:

      print("user = Paper")

   if z==2:

      print("user = Scissors")

   if z==3:

      print("user = Stones")

   
   x = random.choice([1,2,3])
  
  
   if x==1:
 
      print("computer = Scissors")
      
 
   if x==2:
 
       print("computer = Stones")
       
 
   if x==3:
 
       print("computer = Paper")
       
   if z==1 and x==2 or z==2 and x==3 or z==3 and x==1:
        print("Congratulations! You won.")
        no
   if z==1 and x==1 or z==2 and x==3 or z==3 and x==3:
       print("Sorry! Computer wins, Better luck next time.")
       
   if z==1 and x==3 or z==2 and x==1 or z==3 and x==2:
       print("Oops! It's a draw.")
       
   d=input("Do you want to play again? ")
   if d =="no":
       break
   
   
#Teen patti
       
import datetime
       x = datetime.datetime.now()

print(x.year)
x=datetime.datetime.now()

print(x.year)
    
print(x.month)

print(x.strftime("%A"))
  

import datetime

x = datetime.datetime.now()

print(x.strftime("%j"))



       
a="5385"

b=int(a)

try:
    print(x)
    
except:
    print("An un expected orror occured")
    
    
   
       
#Assignment
z="I love India and America"
y=[]

for i in z:
    y.append(i)
    print(y,end='')
    

#Assignment
    
l=[1,2,3,4,5,6,7,8]
k=[i**2 for i in l if i % 2==0] 
print(k)      
def even():
    for i in l:
        if i % 2==0:
            print(i**2)
         
            
l=[1,2,3,4,5,6,7,8] 
x=list(map(lambda x: x**2,filter(lambda x:x%2==0,l)))
#map (function, iterables) above first lambda is the function and filter in this case is the iterable

y=[i for i in l if i %2==0 ]
print(y)

k=list(map(lambda a:a**2,y)) 

    
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

def length(e):
    return len(e)
cars.sort(key=length)
cars.sort(key=length,reverse=True)

f=lambda a,b,c:a*b*c
result=f(4,10,12)
print(result)
   
z=int(input("Enter the number"))

if z <=1:
    print("Enter a valid input")
    
for i in range(2,z):
    if z % i==0:
        print("its not a prime number")
        print(i, "times", z//i, "is", z)
        break
        
else:
    print("prime")
    
    
l=[1,2,3,4,5,5,6,6,7,8,9]
k=list(map(lambda x:x**2,filter(lambda x:x%2==0,l)))

#numbers divisible by 7 in a certain range
y=[]  
d=0
for i in range(2,1000):
    if i % 7 ==0:
        print(i)
        d=d+i
        print(d)
        
#Calculator
try:
        
    u=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    
    while 1:
        p=input("Do you want to add, multiply , subtract or divide two numbers? ")
        
        if p == "add":
            print("Addition is",u+b)
            
        if p == "Subtract":
            print("Subtraction is",u-b)
            
        if p == "Multiply":
            print("Multiplication is",u*b)
            
        if p == "Divide":
            print("Division is",u/b)
            
        z=input("Do you want to quit")
        if z== "y":
            break
    
except ValueError as e:
    print("input number in figure",e)
    
 #Swap the number
a=3
b=2
v=a
a=b
b=v
print(a)
print(b)    

#Rock paper scissors
import random 
  
# using choice() to generate a random number from a  
# given list of numbers. 
print ("A random number from list is : ",end="") 
print (random.choice([1, 4, 8, 10, 3])) 
  
# using randrange() to generate in range from 20 
# to 50. The last parameter 3 is step size to skip 
# three numbers when selecting. 
print ("A random number from range is : ",end="") 
print (random.randrange(20, 50, 3))

    print('provide a random number\n 1 = paper\n 2 = stone\n 3= scissor')
while 1:
        A = int(input('a number' ))
        if A != 1 and A!= 2 and A !=3:   
            print('invalid input quit')
            break
        else: 
            b= (random.choice([1,2,3]))
            print(b)
            if A== 1 and b == 3 or A == 2 and b== 1 or A == 3 and b == 2 :
                print('user lost')
            elif  A== 1 and b == 2 or A == 2 and b == 3 or A ==3 and b== 1:
                print('user won')
            else:
                print('draw')
    
from tkinter import *
d=Tk()
Label(d,text="Entry 1").grid(row=0,column=1)
Label(d,text="Entry 2").grid(row=1,column=1)
Label(d,text="Entry 3").grid(row=2,column=1)


a=Entry(d)
a.grid(row=0,column=2)
b=Entry(d)
b.grid(row=1,column=2)
c=Entry(d)
c.grid(row=2,column=2)


def xyz():
    q=a.get()
    w=b.get()
    t=c.get()
   
    
    fh=open("hi.txt","a")
    fh.writelines([q+",",w+",",t+","+"\n"])
    fh.close()
    fh=open("hi.txt","r")
    print(fh.read())
    
s=Button(d,text="Submit",command=xyz)
s.grid(row=8,column=6)
mainloop()


#converting alternate letters to lower and upper
s="Radha"
#RaDhA
z=""
i=0
for j in s:
    if i % 2==0:
        z+=j.upper()
        
        
    else:
        z+=j.lower()
    i+=1
print(z)

#Pattern
n=5
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()

print("--------------------")

for i in range(n+1):
    for j in range(5-i):
        print("*",end="")
        
    print()

#hello telusko
    
i=1
while i <=5:
    print("Hello",end="")
    
    i=i+1
    j=1
    while j <= 5:
        print("Telusko",end="")
        j=j+1
    print()
    
l=[1,2,3,4,5,6,7,8,9,10,11,12]
x=list(map(lambda x:x**2,filter(lambda x:x%2==0,l)))

   
y=[0,0,0,0]

while 1:
  z=input("In which direction do you want to move and how many steps?")
  d=z.split(" ")
  c=int(d[1])
  if d[0]=="up":
      y[0]=y[0]+c
      print(y)
  
    #practice
z="Ravi Kumar"
y=""
i=0

for j in z:
    if i % 2==0:
        y+=j.upper()
        
    else:
        y+=j.lower()
        
    i+=1 # to increment
        
print(y)

#Practice


def length(e):
    return len(e)
d=['Volvo','Volkswagen','Maruti']
d.sort(key=length,reverse=True)
print(d)

#practice
s=input("enter a string ")
upper=0
lower=0
alpha=0
digit=0

for i in s:
    if i.isupper():
        upper=upper+1
        
    if i.islower():
        lower=lower+1
    
    if i.isdigit():
        digit=digit+1
        
    if i.isalpha():
        alpha=alpha+1
        
print(upper)
print(lower)
print(digit)
print(alpha)
        
        
a=int(input("figure" ))
d=0
while a > 0:
    s = a % 10          #1234, 4,d=4
    d= d + s
    a= a//10
print(d)
    
    
#multiplication of 29

for i in range(1,11):
    print(29*i)
    
#Patterns
for i in range(5):
    for j in range(i):
        print("*",end="")
        
    print()
    
i=1
while i < 6:
    print("Hello",end="")
    
    i=i+1
    j=1
    while j < 6:
        print("telusko",end="")
        j=j+1
        
    print()
 

#Practice
    
i=0
for j in range(1,1001):
    if j % 3==0 or j % 5==0:
        i=i+j
        
print(i)

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?  
d=600851475143
for i in range(2,d+1):
    if d % i==0:
        print(i)
         #6857
        for j in range(2,i+1):
            if i % j!=0:
                print(j)
                break

#sys    
import sys                
    sys.builtin_module_names
    sys.platform
    sys.version
  sys.modules
    sys.getprofile()
    
#Practice    
z=1
print(z)

for i in range (1,21):
        
     if z % i ==0:
        print(i)
z+=1
 
 #LCM
z=int(input("enter first number "))
y=int(input("enter second number ")) 
if z > y:
    z,y=y,z
for i in range(y,y*z+1,y):
      if i % z==0 and i% y==0:
          
          #lcm=i
      #if i % z==0:
          print("LCM is",i)
          break
        
#swapping   
a=2
b=3
a,b=b,a
print("a",a)
print("b",b)
    
 #HCF Highest common factor

x=int(input("Enter the first number "))
k=int(input("Enter the second number "))

if x < k:
    x,k=k,x
#   smaller=k
#   
#else:
#    smaller=x 
for i in range (1,k+1):
    if ((x % i==0) and (k % i==0)):
        hcf=i
print("HCF is",hcf)


#Practice
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

x=1
while i <=20:
    if x % i==0:
        print(x)
        
    x+=1
    

        
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.  
#    
    
    
n=0
a,b=1,1
while a < 4000000:
     if a % 2==0:
         
         n+=a
     a,b=b,a+b
         
print(n)
         
         
    
n = 600851475143
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1

print (n)    
    
#leap yr 
n=int(input('enter the year '))

if n % 4==0 and n % 100!=0 or n % 400==0:
    
    print("Yes this is a leap yr")
    
else:
    print("not a leap yr")
    
#linear and binary search
list=[1,2,3,4,5,6,7]
n=3

if n in list:
    print("Found at",list.index(n))
    
else:
    print("not found")

#list.sort() sorts a list in ascending order

n=[1,4,6,7,343,8,9,3,56,2]
n.sort()
 
#for i in list:
#    if i==list:
#        print("found")
#    else:
#        print("not found")
    
    
  

 
    
    
    
    