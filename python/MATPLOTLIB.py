# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 12:41:19 2019

@author: Ravi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(101)

x=np.arange(0,10)
y=x**2
print(x)
print(y)


plt.plot(x,y)
plt.show()
plt.plot(x,y,'*') # will print graph with *

plt.plot(x,y,'r--')
plt.plot(x,y,'b--') # will plot scattered graph with red colour #r

plt.xlim(3,5) #xrange
plt.ylim(10,20)
plt.title("Zoomed")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.plot(x,y,'r--')


mat=np.random.randint(0,100,(10,10))
plt.imshow(mat,cmap='RdYlBu')

plt.imshow(mat,cmap='seismic')
plt.colorbar()

plt.imshow(mat,cmap='binary')
plt.colorbar()

df=pd.read_csv(r"D:\python\pulsar_stars.csv")
print(df)

#

plt.plot(x=df[' Mean of the integrated profile'],y=[' Standard deviation of the integrated profile'],kind='scatter')
x=df[' Mean of the integrated profile']
y=df[' Standard deviation of the integrated profile']
plt.plot(x,y,'r--')

#Practice

x=np.arange(0,20)
y=x**3

plt.plot(x,y)

plt.xlim(4,8)
plt.ylim(1000,20000)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Zoomed graph")
plt.plot(x,y,'r--')

mat=np.random.randint(1,100,(10,10))
plt.imshow(mat,cmap='RdYlBu')

plt.imshow(mat,cmap='seismic')
plt.colorbar()

plt.imshow(mat,cmap='binary')
plt.colorbar()


df=pd.read_csv(r"D:\python\pulsar_stars.csv")
print(df)

#subplot, bar graphs, scatter

import matplotlib.pyplot as plt
trace=plt.scatter(x=[1,3],y=[4,5])
trace1=plt.scatter(x=[1,3],y=[4,5])
trace2=plt.scatter(x=[6,7],y=[8,9])
#trace3=plt.scatter(x=[1,3,6,7],y=[4,5,8,9])

plt.ylabel("Y")
plt.xlabel("X")
plt.title("my graph")
plt.plot([1,2,3,4],[1,4,9,16]) # x=x, y = x**2

plt.show()
plt.plot([1,2,3,4],[1,4,9,16],'r--')
plt.show()

import numpy as np
t=np.arange(0,5,0.2)
print(t)

#red dashes, blue circles and green triangles

plt.plot(t,t,'r--',t,t**2,'bo',t,t**3,'g^')
plt.show() #prints

names=['group a','group b','group c']
values=[1,10,100]

plt.subplot(131) #1,3,1
plt.bar(names,values) #names= x, values = y

plt.subplot(132)
plt.scatter(names,values)

plt.subplot(133)
plt.plot(names,values)

#plt.subplot(134)
#plt.plot(names,values) error

plt.suptitle("Categorical Plotting")
plt.show()

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t) #radian = pi

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)
print(t1,t2)

plt.plot(t2,f(t2),'k')
plt.plot(t1,f(t1),'bo')
plt.figure() #describes the size of the figure

plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.show()

x=['Ravi','Shubham','Vijay']
y=[200, 300, 400]

plt.xlabel("Employee")
plt.ylabel("Salary")

plt.subplot(311)
plt.scatter(x,y)

plt.subplot(312)
plt.bar(x,y)

plt.subplot(313)
plt.plot(x,y)

plt.suptitle("Categorical plotting")

t=np.arange(0,10)

plt.plot(t,t,'r--',t,t**2,'bo',t,t**3,'g^')
plt.show()

t1=np.arange(0,5,0.1)
t2=np.arange(0,5,0.01)

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

plt.plot(t2,f(t2),'k')
plt.plot(t1,f(t1),'bo')
plt.figure()

plt.plot(t1,f(t1),'bo',t2,f(t2),'k')
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.show()

t=np.cos(2*np.pi*t2)
print(t)

t=np.cos(2*np.pi*0.01)
print(t)
































