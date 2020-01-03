# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:08:48 2019

@author: Ravi
"""

#messagebox

from tkinter import *
from tkinter import messagebox as mb

def answer():
    mb.showerror("Answer","Sorry, no answer available")
    
def callback():
    if mb.askyesno('Verify','Really quit?'):
        mb.showwarning("yes","not yet implemented")
    else:
        mb.showinfo('No','Quit has been cancelled')
        
Button(text='Quit',command=callback).pack(fill=X)
Button(text='Answer',command=answer).pack(fill=X)

mainloop()


#scrollbar

from tkinter import *

def show_values():
    print(w1.get(),w2.get())
    
    
master= Tk()
w1=Scale(master,from_=0,to=80,tickinterval=20)
w1.set(19)
w1.pack()
w2=Scale(master,from_=0, to=200,tickinterval=10,orient=HORIZONTAL)
w2.set(29)
w2.pack()
Button(master,text="Show",command=show_values).pack()
mainloop()


#FileDialog
import os

from tkinter import *
from tkinter.filedialog import askopenfilename

def callback():
    name=askopenfilename()
    os.startfile(name)
    print(name)
    
errmsg="Error!"
Button(text="filopen",command=callback).pack(fill=X)
mainloop()



#File dialog box with options


from tkinter import *
from tkinter.filedialog import askopenfilename

def newfile():
    print("New File")

def openfile():
    name=askopenfilename()
    print(name)
    
def about():
    print("This is a simple example of menu")
    
root=Tk()
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command = newfile)
filemenu.add_command(label="open",command=openfile)
filemenu.add_separator()
filemenu.add_command(label="exit",command=root.quit)

helpmenu=Menu(menu)
menu.add_cascade(label="help",menu=helpmenu)
helpmenu.add_command(label="about",command=about)
mainloop()



#PRactice

from tkinter import *
from tkinter import messagebox as mb

def answer():
    mb.showerror("Sorry!","Answer not yet available")
    
def callback():
    if mb.askyesno("Verify","do you want to quit"):
        mb.showerror("Yes","not yet implemented")
        
    else:
        mb.showinfo("No","Quit has been cancelled")
        
Button(text="Answer",command=answer).pack(fill=X)
Button(text="Quit",command=callback).pack(fill=X)

mainloop()

#filedialog
from tkinter import  *
from tkinter.filedialog import askopenfilename

def yo():
    v=askopenfilename()
    print(v)

errmsg="Error!"
Button(text="Submit",command=yo).pack(fill=X)
mainloop()


#Scrollbar

from tkinter import *
def z():
    print(t1.get(),t2.get())
    
d=Tk()

t1=Scale(d, from_=0, to=80, tickinterval=20)
t1.set(15)
t1.pack()
t2=Scale(d,from_=0, to=100, tickinterval=30,orient=HORIZONTAL)
t2.set(20)
t2.pack()

Button(d,text="Print",command=z).pack()

mainloop()


#Radiobutton

import tkinter as tk
root =tk.Tk()
v=tk.IntVar() #V will hold integer values

def k():
    print(v.get())
    
a=tk.Label(root,text="Choose a programming language",padx=20).pack()
b=tk.Radiobutton(root,text="Python",padx=20,variable=v,value=1).pack()
#as soon as user clicks on python v.get() will become 1
c=tk.Radiobutton(root,text="R",padx=20,variable=v,value=2).pack()
d=tk.Button(root,text="Print",padx=20,command=k).pack()

root.mainloop()

#PRACTICE
from tkinter import *
from tkinter.filedialog import askopenfilename
def newfile():
    print("Let's open a new file")
def openfile():
    h=askopenfilename()
    print(h)
def about():
    print("This is a simple example of menu")

root=Tk()
menu=Menu(root) #creates a menu window inside the tkinter window
root.config(menu=menu) #configures that you want to use menu, default value is(menu=null)
filemenu=Menu(menu) #you want to create a file menu inside the menu window
menu.add_cascade(label="File",menu=filemenu) #menu that you want to use inside the File button
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
helpmenu=Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About",command=about)

mainloop()
    
#radiobutton
import tkinter as tk
root=tk.Tk()
d=tk.IntVar()
def new():
    print(d.get())
    
#if d.get is python then intvar will hold the value 1
    
tk.Label(root,text="Choose your gender").pack()
tk.Radiobutton(root,text="Male",variable=d,value=1).pack()
tk.Radiobutton(root,text="Female",variable=d,value=2).pack()
tk.Button(root,text="Enter",command=new).pack()
mainloop()
    
#File
import os
from tkinter import *
from tkinter.filedialog import askopenfilename
root=Tk()
root.title("PRactice")
def newfile():
    print("This option will create a new file")
    
def opnefile():
    name=askopenfilename()
    os.startfile(name)
    print(name)
    
def about():
    print("This is  how you make two windows")
    
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=opnefile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
helpmenu=Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About",command=about)
mainloop()
    
#messagebox
from tkinter import *
from tkinter import messagebox as mb
root=Tk()
def answer():
    mb.showerror("Error!","Answer not yet implemented")
   
def quit():
    if mb.askyesno("Verify","Really quit?"):
        mb.showwarning("Warning!","Quit not yet implemented")
        
    else:
        mb.showinfo("Yo","Quit has been cancelled")
Button(root,text="Answer",command=answer).pack()
Button(root,text="Quit",command=quit).pack()
mainloop()

        #Practice
import os        
from tkinter import *
from tkinter.filedialog import askopenfilename
root=Tk()

def xyz():
    print("Open new file")
    
    
    
def openfile():
    name=askopenfilename()
    os.startfile(name)
    print(name)
    
def about():
    print("This is how you open a file")
    
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=xyz)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
helpmenu=Menu(menu)
menu.add_cascade(label="help",menu=helpmenu)
helpmenu.add_command(label="about",command=about)
mainloop()

#radiobutton
import tkinter as tk
root=tk.Tk()
d=tk.IntVar()
def my():
    print(d.get())

tk.Label(root,text="Choose your gender").pack()
tk.Radiobutton(root,text="Male",variable=d,value=1).pack()
tk.Radiobutton(root,text="Female",variable=d,value=2).pack()
tk.Radiobutton(root,text="None of the above",variable=d,value=3).pack()
tk.Button(root,text="Submit",command=my).pack()
tk.mainloop()

#Scrollbar
from tkinter import *
d=Tk()
d.title("ScrollBar")
d.geometry("500x500")
def yo():
    print(w1.get(),w2.get())
    
w1=Scale(d, from_=0, to=80, tickinterval=20)
w1.set(15)
w1.pack()
w2=Scale(d,from_=20, to=200,tickinterval=20,orient=HORIZONTAL)
w2.set(40)
w2.pack()
w3=Button(d,text="print",command=yo)
w3.pack()
mainloop()


#checkbutton
from tkinter import *
root=Tk()
root.config(background="black")
var1=IntVar()
Checkbutton(root,text="Male",variable=var1).grid(row=0)

var2=IntVar()
Checkbutton(root,text="Female",variable=var2).grid(row=1)

def xyz():
    print(var1.get(),var2.get())

Button(root,text="Submit",command=xyz).grid(row=3)

mainloop()

#Radiobutton
from tkinter import *
root=Tk()
d=IntVar()
def xyz():
    print(d.get())

Label(root,text="Choose your gender").grid(row=0)
    
Radiobutton(root,text="Male",variable=d,value=1).grid(row=1)
Radiobutton(root,text="FeMale",variable=d,value=2).grid(row=2)

Button(root,text="Ok",command=xyz).grid(row=3)
mainloop()


from tkinter import *
root=Tk()
root.title("Scrollbar")
w1=Scale(root,from_=20,to_=80,tickinterval=20)
w1.set(15)
w1.pack()
w2=Scale(root,from_=0,to_=100,tickinterval=20,orient=HORIZONTAL)
w2.set(30)
w2.pack()

def xyz():
    print(w1.get(),w2.get())
    
s=Button(root,text="Submit",command=xyz)
s.pack()

mainloop()





























