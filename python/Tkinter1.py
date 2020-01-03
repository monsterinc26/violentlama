# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:28:45 2019

@author: Ravi
"""

#TKINTER

import tkinter as tk

r=tk.Tk()

r.title("GUI")
button=tk.Button(r,text="Stop",width=25,command=r.destroy)
button.pack()

def fun():
    print("as")
    
button1=tk.Button(r,text="hello",width=25,command=fun)
button1.pack()

r.mainloop()

#Labels and buttons

from tkinter import *
d=Tk()
Label(d,text="First Name").grid(row=0)
Label(d,text="Last Name").grid(row=1)
e1=Entry(d)
e2=Entry(d)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

def func():
    print(e1.get(),e2.get())
    
b1=Button(d,text="submit",command=func)
b1.grid(row=4,column=5)

mainloop()


#Assignment, Calculator


    

from tkinter import *
    
z=Tk()
    
Label(z,text="Enter the first number").grid(row=0)
Label(z,text="Enter the second number").grid(row=1)
    
r1=Entry(z)
r2=Entry(z)

r1.grid(row=0,column=1)
r2.grid(row=1,column=1)
    
def myfunc():
    try:
             a=int(r1.get())
             b=int(r2.get())
            
             print("Addition","is",a+b)
    except ValueError as e:
         print("the error is ",e)
    
def newfunc():
    try:
     a=int(r1.get())
     b=int(r2.get())

     print("Subtraction","is",a-b)
     
    except ValueError as e:
        print("the error is",e)
        
def func():
        try:
            a=int(r1.get())
            b=int(r2.get())
          
            if(b>=0):
                print("Multiplication","is",a*b)
                
            elif a>=0:
                print("Multiplication","is",a*b)
                
            else:
                print("invalid input because multiplying anything by 0 is 0")
        except ValueError as e:
            print("error is ",e)
            
def ohfunc():
    try:
         
         a=int(r1.get())
         b=int(r2.get())
         if a==0:
             print("Aything dividing 0 will give the result 0")
         elif b==0:
             print("Anything divided by 0 is infinity")
             
         else:
             print("Division","is",a/b)
                
    except ValueError as e:
        print("the error is",e)
         
b1=Button(z,text="Subtract",command=newfunc)
b1.grid(row=3,column=2)
b2=Button(z,text="Add",command=myfunc)
b2.grid(row=3,column=3)
b3=Button(z,text="Multiply",command=func)
b3.grid(row=3,column=4)
b4=Button(z,text="Divide",command=ohfunc)
b4.grid(row=3,column=5)
    
mainloop()
#        
#except ValueError as e:
#    print("the error is",e)
    

#Assignment  

from tkinter import *
d=Tk()


Label(d,text="First Value").grid(row=0)
Label(d,text="Second Value").grid(row=1)
Label(d,text="Third value").grid(row=2)
Label(d,text="Fourth Value").grid(row=3)

c=Entry(d)
c.grid(row=0,column=2)
f=Entry(d)
f.grid(row=1,column=2)
g=Entry(d)
g.grid(row=2,column=2)
h=Entry(d)
h.grid(row=3,column=2)

def funcc():
    a=c.get()
    b=f.get()
    i=g.get()
    k=h.get()
    
    
    fh=open("hi.txt","a")
    fh.write(a+",")
                        #we can also use writelines([a,b,i,k]) then use comma with each variable and \n at the last
    fh.write(b+",")
    
    fh.write(i+",")
    
    fh.write(k+","+"\n")
    fh.close()
    fh=open("hi.txt","r")
    print(fh.read())
    
s=Button(d,text="submit",command=funcc)
s.grid(row=6,column=7)


mainloop()
    

from tkinter import *

f=Tk()
f.title("Calculator")

Label(f,text="Enter first number").grid(row=0)
Label(f,text="Insert second number").grid(row=1)

t1=Entry(f,bg="black",fg="white") 
t2=Entry(f,bg="black",fg="white")
t1.grid(row=0,column=0)
t2.grid(row=1,column=1)

def j():
    try:
        
     a=int(t1.get())
     b=int(t2.get())
     print("Addition","=",a+b)
     
    except ValueError as e:
        print("The error is",e)
    
def k():
    try:
     a=int(t1.get())
     b=int(t2.get())
     print("Subtraction","=",a-b)
     
    except ValueError as e:
        print("The error is",e)
        
    
def l():
    try:
     a=int(t1.get())
     b=int(t2.get())
     if a > 0:
        print("Multiplication","=",a*b)
     elif b > 0:
         print("Multiplication","=",a*b)
     else:
         print("anything multiplied by 0 is 0")
         
    except ValueError as e:
        print("The error is",e)
    
def y():
    try:
     a=int(t1.get())
     b=int(t2.get())
     if a==0:
         print("0 divided by anything gives result 0")
         
     elif b==0:
         print("Anything divided by 0 gives infinity")
         
     else:
         print("Division","=",a/b)
         
    except ValueError as e:
        print("The error is",e)
        
    
b1=Button(f,text="Add",command=j)
b1.grid(row=3,column=2)
b2=Button(f,text="Subtract",command=k)
b2.grid(row=3,column=3)
b3=Button(f,text="Multiply",command=l)
b3.grid(row=3,column=4)
b4=Button(f,text="Divide",command=y)
b4.grid(row=3,column=5)

mainloop()
    







