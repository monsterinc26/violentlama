# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:50:18 2019

@author: Ravi
"""

import numpy as np
import pandas as pd
np.random.seed(101)

"""
pd series

"""
labels=['a','b','c']
mylis=[10,20,30]
arr=np.array(mylis)

a=pd.Series(data=mylis,index=labels)
print(a)
#or
b=pd.Series([10,20,30],['a','b','c'])

mylis2=pd.Series(range(0,3),labels) # if you take range more than 3 then you dont need to write labels
print(mylis2)
#dictionary
d={'x':10,'y':20,'z':30} #keys will be treated as indexes and values will be the data
mylis3=pd.Series(d)
print(mylis3)

"""
pd dataframes

"""

matrix=[[1,2,3],[4,5,6],[7,8,9]]
q=np.array(matrix)
print(q)

dataframe=pd.DataFrame(data=q,columns=['a','b','c'],index=['x','y','z'])
print(dataframe)

dataframe2=pd.DataFrame(np.random.randn(3,3),['a','b','c'],['x','y','z'])#by default it will take index first
print(dataframe2)

df=pd.DataFrame(np.random.rand(3,3),['a','b','c'],['x','y','z'])

"""
index

"""

q1=dataframe[['a','b']]
print(q1)

print(df>0)

w=df['x']
print(w)
#g=df[['a','x']]

qa='1 2 3'.split()
print(qa) #create list

df['state']=qa
print(df) #add row qa and tag state #this will add one column that is state and qa will add row values i.e.[1,2,3]

z=df.set_index('state')
print(z)

q="pdunlap@yahoo.com, anthony41@reed.com"
i=q.split('@')
print(i)
w=i[1][0]


#data input output


q=pd.read_csv("~Ravi Singh/Downloads/example.csv")
print(q)

"""

While importing the file use forward slash/not backward slash it causes error


"""
#importing excel file

w=pd.read_excel(r"D:\Data Analyst\MIS\2nd Jan Batch 11.30 Day6.xlsx",sheet_name="Left")

print(w)

#/-backward
#\-forward

w.head(10)
w.info()


y=[1,2,3]
er=np.array(y)
x=[['x','y','z']]
df=pd.Series(data=er,index=x)
print(df)

df=pd.Series([1,2,3],['a','b','c'])
print(df)

df=pd.Series(range(0,3),['a','b','c'])
print(df)

d={'x':10,'y':20,'z':30}
df=pd.Series(d)
print(df)


matrix=[[1,2,3],[4,5,6],[7,8,9]]
f=np.array(matrix)
df=pd.DataFrame(data=f,columns=['a','b','c'],index=[0,1,2])
print(df)


df2=pd.DataFrame(np.random.randn(3,3),[0,1,2],['x','y','z'])
print(df2)

df3=pd.DataFrame(np.random.rand(3,3),[0,1,2],['x','y','z'])
print(df3)


q1=df[['a','b']]
print(q1)
w=df2['x']
df2['State']=[4,5,6]
print(df2)


#multi indexing in pandas and handling null values

df=pd.DataFrame(np.random.randn(3,3),['a','b','c'],['x','y','z'])
print(df)


df=pd.DataFrame(np.random.randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)

df['new']=df['W']+df['Y'] #this will add values of W and Y columns and put in 'new'column
print(df)

df.drop('new',axis=1) #will delete column new, axis =1 for columns
df.drop('E',axis=0)

df.loc['A'] #This will print the row A i.e. works on index labels
df.iloc[2] #This will print row number 2 i.e. works on position (starts from 0)

df.loc['B','Y']# value which lies under Bth row and Yth column
df.loc[['A','B'],['W','Y']] # will print [A,W],[A,Y],[B,W],[B,Y]

"""
Multi index and index hierarchy
Multi indexed and data frame

"""
#indexlevels
outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]


innerindex=list(zip(outside,inside))
innerindex=pd.MultiIndex.from_tuples(innerindex) #converts innerindex into an array

df=pd.DataFrame(np.random.randn(6,2),index=innerindex,columns=['A','B'])
df.loc['G1']
df.loc['G1'].loc[1,'A']
df.loc['G1']['A'].loc[1]
df.loc['G1']['A'].iloc[1]

#nullvalues filling and removing missing or null values

d={'a':[1,np.nan,2],'b':[1,np.nan,np.nan],'c':[1,2,3]} # keys will be columns
df=pd.DataFrame(d)
print(df)
q=df.dropna() # sometimes deletes the whole row if it has null values
print(q)

q=df.fillna('123') #fills the null value with 123
print(q)
print(df)

values={'a':0,'b':1,'c':2} #fill value as per column names in df
q=df.fillna(values)
print(q)
print(q[['a','b']]) # will print columns a and b in q

q=df['a'].fillna(value='abc') #this fills the numm value in a specific column
print(q)
print(df)

z=df.loc[1,'a']=5 # will change the null value to 5, 1st row and a column
print(z)
print(df)

#importing csv files from the website

"""
conda install lxml
conda install html5lib
conda install BeautifulSoup4

"""

r=pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

c=pd.DataFrame(data=r)
print('hi i am variable r',r)


df=pd.DataFrame(np.random.randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)

df['new']=df['W']+df['Y']
print(df)

df.drop('new',axis=1)
df.drop('E',axis=0)
df.loc['A']
df.iloc[2]
df.loc['B','Y']
df.loc[['D','E'],['Y','Z']]

outside=['g1','g1','g1','g2','g2','g2']
inside=[1,2,3,1,2,3]
index1=list(zip(outside,inside))
index2=pd.MultiIndex.from_tuples(index1)
data=pd.DataFrame(np.random.randn(6,2),index=index2,columns=['A','B'])
print(data)

data.loc['g1']
data.loc['g1'].loc[1,'A']
data.loc['g2','A'].loc[2]
data.loc['g2','A'].iloc[2]

d={'x':[1,np.nan,2],'y':[1,2,np.nan],'z':[np.nan,1,2]}
df=pd.DataFrame(d)
print(df)

q=df.dropna()
print(q)
w=df.fillna(132)
print(w)

values={'a':1,'b':2,'c':3}
w=df.fillna(values)
print(w)
print(w[['a','b']]) #ask this doubt
q=df['a'].fillna('123')
print(q)

df.loc[1,'a']=5
print(df)

#df.mean() , df.mode(),df.info(),df.isnull(),df.describe(),df.groupby()

r=pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
print(r)

df=pd.DataFrame(data=r)

f=pd.read_csv(r"D:\python\pulsar_stars.csv")
print(f)

df=pd.DataFrame(data=f)
print(df)

v=df.mean()
print(v)

z=df.mode()
print(z)

df.info()#returns information
df.isnull() #retuns boolean

df.describe()
df.groupby(by=" Mean of the integrated profile").mean()

#join, concat, groupby
data={'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Ravi','Sam','Sandeep','Amy','Vanessa','Shubham'],
       'Sales':[200,120,340,124,243,350]}
df=pd.DataFrame(data)
by_comp=df.groupby("Company")
df.mean() ### check
by_comp.mean()
#df.groupby("Company").mean()
by_comp.std()
by_comp.min()
by_comp.max()
by_comp.count()
by_comp.describe()
by_comp.describe().transpose()  #create 1*n view for describe method #row to column, column to row

df1=pd.DataFrame({'A':['A0','A1','A2','A3'],
                  'B':['B1','B2','B3','B4'],
                  'C':['C1','C2','C3','C4'],
                  'D':['D1','D2','D3','D4']},
                   index=[0,1,2,3] )

df2=pd.DataFrame({'A':['A4','A5','A6','A7'],
                  'B':['B4','B5','B6','B7'],
                  'C':['C4','C5','C6','C7'],
                  'D':['D4','D5','D6','D7']},
                    index=[4,5,6,7])

df3=pd.DataFrame({'A':['A8','A9','A10','A11'],
                  'B':['B8','B9','B10','B11'],
                  'C':['C8','C9','C10','C11'],
                  'D':['D8','D9','D10','D11']},
                    index=[8,9,10,11])


print(df1,df2,df3)
z=pd.concat([df1,df2,df3])
print(z)
z=pd.concat([df1,df2,df3],axis=1)
print(z)

#joining

left=pd.DataFrame({'A':['A0','A1','A2'],
                   'B':['B0','B1','B2']},
                     index=['K0','K1','K2'])
right=pd.DataFrame({'C':['C0','C1','C2'],
                    'D':['D0','D1','D2']},
                     index=['K0','K2','K3'])
print(right.join(left))
print(left.join(right))

#Practice
f=pd.read_csv(r"D:\python\pulsar_stars.csv")
print(f)

df=pd.DataFrame(f)
print(df)

z=df.groupby(" Mean of the integrated profile")
print(z)
z.mean()
z.std()
z.min()
z.max()
z.describe()







