# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:12:25 2019

@author: Ravi
"""
import numpy as np
import random

np.random.seed(20) # This will generate random for only one time

mylist=[[1,2,3],[4,5,6],[7,8,9]]
print(mylist)
q=np.array(mylist)

w=np.array(range(10))
print(w)

e=np.arange(0,10) # can be used insted of array and range
print(e)

r=np.arange(0,10,2)
print(r)

t=np.zeros([2,3])
print(t) # 2 and 3 are the respective number of rows and columns

z=np.ones([3,3])
print(z)

u=np.linspace(0,5,10)
print(u)

i=np.eye(3,3)
print(i)

o=np.random.rand(4,4) #gives random array of size 4*4
print(o)

p=np.random.randint(1,10,size=(3,3))
print(p)

p=np.random.randint(1,70,20)
print(p)

p=p.reshape(5,4)
print(p)

p.max()
p.min()
p.mean()

sg=np.array([[1,2,3],[4,5,6],[7,8,9]])
d=sg[0:1,0:2]
print(d)

dg=sg[:,-1]
print(dg)
print(sg)

bool_array=sg > 4 #give bools
print(bool_array)

f=np.arange(50).reshape(5,10)
print(f)

g=f+100
h=f**2
print(g,h)

j=np.sqrt(f)
print(j)

j=np.exp(f)
print(j)

j=np.cos(f)
print(j)

j=np.sin(f)
print(j)

x=np.random.randint(1,9,size=(3,3))
print(x)

for i in range(len(x)):
   for j in range(len(x[i])):
       print(x[i][j],end="")
   print()
   
for i in x:
       for j in x[i]:
           print(x[i][j],end="")
       print()


x=np.random.randint(1,9,size=(3,3))
print(x)
a=x[0:,1]
print(a)

x=np.random.randint(1,9,size=(3,3))
print(x)
for i in x:
    #print(i)
    
    for j in i:
        print(j,end="")
        
    print()
        
x=np.random.randint(1,9,size=(3,3))
print(x)    

x[1,:]
x[0:1,0:2]
x[0:2,1]

#frooti

arr=[0,1,0.5,1]
print("array input",arr)
#This function is used to calculate the inverse cos of the array elements.
arccos_val=np.arccos(arr)
print("cos inverse is",arccos_val)

arccos_val=np.arcsin(arr)
print("sin inverse is",arccos_val)

arccos_val=np.arctan(arr)
print("tan inverse is",arccos_val)

#this function is used to convert the angles from radian to degrees.

import math

arr=[0,math.pi/2,math.pi/4,math.pi/6]
degval=np.degrees(arr)
print(degval)

tanarr=np.tan(degval)
print(tanarr)

radval=np.deg2rad(arr)
print("\n Radian value : \n",radval)


#This function is used to calculate the hypotenuse for the right angled triangle.The hypotenuse of the right angle is calculated as.

base=[10,2,25,50]
per=[3,10,23,6]

print("input base array:",base)
print("input perpendicular array:",per)

hyp=np.hypot(base,per)
print("hypotenuse ",hyp)

np.hypot(6,4)
#radian to degree
degval=np.rad2deg(arr)
print("\n degree value : \n",degval)

#hyperbolic
arcsinh()
import math
import random
import numpy as np
arr=np.random.randint(1,20,size=(3,3))
print(arr)

u=[0,math.pi/2,math.pi/4,math.pi/6]
y=np.degrees(u)
y=np.rad2deg(u)
z=np.deg2rad(u)
t=np.tan(y)

x=np.rad2deg(u)

 





