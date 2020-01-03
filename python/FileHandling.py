# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:12:46 2019

@author: Ravi
"""

# FILE HANDLING

fh=open("hi.txt","r")
print (fh.read())

fh=open("hi.txt","r")
print (fh.readlines(6))

fh=open("hi.txt","a")
fh.write("Welcome to the jungle")
fh.close()

fh=open("hi.txt","r")
print(fh.read())

fh=open("hi.txt","w")
fh.write("Welcome to the jungle")
fh.close()

fh=open("hi.txt","r")
print(fh.read())

#Assignment

a=int(input("enter the number "))

d=0
#^
#initilaizing a variable with 0

while a > 0:
    
#running a loop to traverse through every digit
    
    x=a % 10
    
    a=a//10     #or you can also use num=int(num/10) 
    
    d+=x
    
               # for step by step printing, type print below d
    
print("sum of digits is",d)

#ID
    
d="Apple"

for i in d:
    print(i,"=", id(i))
    
#File Handling

fh=open("hello.txt","r")
print(fh.read())

fh=open(r"C:\Users\Ravi\.spyder-py3\hello.txt","r")
print(fh.readline())

fh=open("hello.txt","r") # Read the contents of the file
for i in fh:
    print(i)
    
fh=open("hello.txt","a") #Append new content in the file from the last word
fh.write(" Welcome to playsound library")
fh.close()   
    
fh=open("hello.txt","r")
print(fh.read())   

fh=open("hello.txt","w") #Clears the previous content and add totally new lines
lines_of_text=["Text line 1","Text line 2","Text line 3"]
fh.writelines("lines of text")
fh.close()
    
fh=open("hello.txt","r")
print(fh.read())

fh=open("hello.txt","r")
print(fh.readlines(2))


fh=open("hi.txt","x") #Creates a new file in the directory, throws a error if the file already exists.
fh.close()

#ALWAYS CLOSE THE RESOURCES YOU OPEN, AS IT KEEPS YOUR SOFTWARE CLEAN AND LIGHT!!!!!!!



number = 43979349347

name= "My name is John and my phone number is {}."

print(name.format(number))


# multiplication of 24, 29 and 50

i = 1

while i<=10:
    
     a= 24*i 
     
     print(a)
     
     i=i+1
     
     
i = 1

while i <=10:
    
    print(29*i)
    
    i=i+1
    

i = 1

while i <= 10:
    
    print(50*i)
    
    i= i + 1
    

#practice
    
a=[1,2,3,4,5,6,7,8,9]

for i in a:
     if i> 5:
         print(i)
         break
         i=i+1
         
#HCF 
         
x=int(input("enter the first number"))

y=int(input("enter the second number"))

while y > 1:
    
    x= x % y
    
    if x % y == a:
        
          b=   y % a
         
          print(b)
        
        
    
    y= y % y
    
    print(x)
    

try:
    print(t)
    
except:
    print("go on")
    
try:
    print(g)
    
except :
    print("something went wrong")
    
except:
    print("Nothing is wrong")



#some of the errors are ValueError, NameError, ZeroDivison Error,etc.
#runtime error, compile error, logical error
    
fh=open("hi.txt","r")
fh.read() 
 
    
 

    
    
 



   
    
    
