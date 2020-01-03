# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 22:50:26 2018

@author: Rochak Sharma
"""


list1=[1,"rp","sda"]
print(list1)
list1[1]="data"
print(list1)
t=(4,4,5,8,58)
#t[1]="saa"
print(t)
a="rochak"
b="sharma"
d={'key1':a,'key2':b}
print(d['key1'],d['key2'])
z={'key1':{'innerkey':"students rocks"}}
print(z['key1']['innerkey'][0])
print(z['key1'],"i am key 2 ",z['key1']['innerkey'])
''' tuples'''
tupple=(7,2,3)
v=tupple[0]
print(v)
''' key diff btwn tupple and list tupple is immuatable or editable but list is editable'''
'''' tupple[0]=4 << error throw'''
'''set'''
'''set give non repeatable value'''
n=set([4,4,4,2,2,5,5,7])
""" OR """
n={1,1,1,2,2,2,4,4}
print(n)
n.add(9) #<< add value to set
print(n)

# '''comaparision''''

# print('bye'='hello')

if 1<2:
     print('yep')
    
if 1==2:
    print('first')
elif 1==1:
    print('me')
else:
    print('second')  

seq=[1,2,3,4,8]
for num in seq:
    print(num*2)
    print('hello')
    
z=input("input number")
z=int(z)
print(z+1);
i=1
while i<5:
    print(i)
    i=i+1

#range()
m=list(range(0,10))   # it make list from 0to10
#print("hi this is m",m)
for x in range(0,10):   
    print(x)
#functions   
def my_func(param1):
    print(param1)
   
my_func('hello')
print(my_func)
def add(a,b):
    print(a+b)
print("enter first number")
z=int(input())
print("enter second number")
w=int(input())
add(z,w)
def square(num):
    """
    this is multiline comment
    """
    return num**2
print(square(4))



























