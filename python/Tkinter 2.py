# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:52:59 2019

@author: Ravi
"""

from tkinter import *

d=Tk()

d.title("Calculator")

Label(d,text=" ").grid(row=0)

a=Entry(d,textvariable=equation)

a.grid(row=0,column=1)


expression = ""
def ffunn(number):

    global expression
    expression = expression + str(number)
    equation.set(expression)
def button_equal():
    try:
 
        global expression
        total = str(eval(expression))
 
        equation.set(total)
        expression = ""
        f=open("myfile.txt","a")
        f.write(total)
        f.write("\n")

    except:
 
        equation.set(" error ")
        expression = ""
 
 
def button_clear():
    global expression
    expression = ""
    equation.set("")
    
equation = StringVar()

 
equation.set('enter your expression') 
    
button1=Button(d,text="1",command=lambda:ffunn(1))
button2=Button(d,text="2",command=lambda:ffunn(2))
button3=Button(d,text="3",command=lambda:ffunn(3))
button4=Button(d,text="4",command=lambda:ffunn(4))
button5=Button(d,text="5",command=lambda:ffunn(5))
button6=Button(d,text="6",command=lambda:ffunn(6))
button7=Button(d,text="7",command=lambda:ffunn(7))
button8=Button(d,text="8",command=lambda:ffunn(8))
button9=Button(d,text="9",command=lambda:ffunn(9))
button0=Button(d,text="0",command=lambda:ffunn(0))
button_add=Button(d,text="+",command=lambda:ffunn("+"))
button_subtract=Button(d,text="-",command=lambda:ffunn("-"))
button_multiply=Button(d,text="*",command=lambda:ffunn("*"))
button_divide=Button(d,text="/",command=lambda:ffunn("/"))
button_equal=Button(d,text="=",command=button_equal)
button_clear=Button(d,text="Clear",command=button_clear)

button1.grid(row=1 ,column=1)
button2.grid(row=1 ,column=2)
button3.grid(row=1 ,column=3)
button4.grid(row=2 ,column=1)
button5.grid(row=2 ,column=2)
button6.grid(row=2 ,column=3)
button7.grid(row=3 ,column=1)
button8.grid(row=3 ,column=2)
button9.grid(row=3 ,column=3)
button0.grid(row=4 ,column=3)
button_add.grid(row=5 ,column=1)
button_subtract.grid(row=5 ,column=2)
button_multiply.grid(row=5 ,column=3)
button_divide.grid(row=6 ,column=1)
button_equal.grid(row=7 ,column=2)
button_clear.grid(row=8,column=2)

mainloop()


a=int(input("Enter the number"))

b=0

while a > 0:
    
    d=a % 10
    
    b=b + d
    
    a=a//10
    
print(b)


 
 


    
from tkinter import *
expression = ""
def press(num):

    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
    try:
 
        global expression
        total = str(eval(expression))
 
        equation.set(total)
        expression = ""
        f=open("myfile.txt","a")
        f.write(total)
        f.write("\n")

    except:
 
        equation.set(" error ")
        expression = ""
 
 
def clear():
    global expression
    expression = ""
    equation.set("")
 
 

root = Tk()

root.configure(background="light green")
 
# set the title of root window
root.title("Simple Calculator")

root.geometry("265x150")

equation = StringVar()
expression_field = Entry(root, textvariable=equation)  
expression_field.grid(columnspan=4, ipadx=70)
 
equation.set('enter your expression')  
button1 = Button(root, text=' 1 ', fg='black', bg='red',
                 command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)
 
button2 = Button(root, text=' 2 ', fg='black', bg='red',
                 command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)
 
button3 = Button(root, text=' 3 ', fg='black', bg='red',
                 command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)
 
button4 = Button(root, text=' 4 ', fg='black', bg='red',
                 command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)
 
button5 = Button(root, text=' 5 ', fg='black', bg='red',
                 command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)
 
button6 = Button(root, text=' 6 ', fg='black', bg='red',
                 command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)
 
button7 = Button(root, text=' 7 ', fg='black', bg='red',
                 command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)
 
button8 = Button(root, text=' 8 ', fg='black', bg='red',
                 command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)
 
button9 = Button(root, text=' 9 ', fg='black', bg='red',
                 command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)
 
button0 = Button(root, text=' 0 ', fg='black', bg='red',
                 command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)
 
plus = Button(root, text=' + ', fg='black', bg='red',
              command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)
 
minus = Button(root, text=' - ', fg='black', bg='red',
               command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)
 
multiply = Button(root, text=' * ', fg='black', bg='red',
                  command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)
 
divide = Button(root, text=' / ', fg='black', bg='red',
                command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)
d1 = Button(root, text=' ( ', fg='black', bg='red',
                command=lambda: press("("), height=1, width=7)
d1.grid(row=6, column=1)
d2 = Button(root, text=' ) ', fg='black', bg='red',
                command=lambda: press(")"), height=1, width=7)
d2.grid(row=6, column=2)  
 
equal = Button(root, text=' = ', fg='black', bg='red',
               command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)
 
clear = Button(root, text='Clear', fg='black', bg='red',
               command=clear, height=1, width=7)
clear.grid(row=5, column='1')
 
root.mainloop()


def is_leap(year):
    

    return year % 4 ==0 and (year % 100!=0 or year % 400==0)

    
    # Write your logic here
    
        

year = int(input())
print(is_leap(year))

n = int(input("Enter"))
print(*range(1, n+1), sep="") # "*"is used to unpack a range or dictionary



d=[1,2,3,4,5,6,7]
d[:4]
d.count(1)
d[::-1]
y=[]
for i in d:
    y.append(i)
print(y)


z="ravi is my name"
z.split()


y=int(input("Enter a number"))

for i in range(0,y+1):
    y={i:i**i}
    print(y)










    
       