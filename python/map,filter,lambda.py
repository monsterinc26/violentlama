"""
mapping and filter function
"""
def square(num):
    """
    this is multiline comment
    """
    return num**2
"""
mapping is used to assign square function in sequence variable
"""

seq=[1,2,3,4,5]
q=map(square,seq)
w=list(map(square,seq))
print(q)
print(w)

e=list(map(lambda num:num**3,seq))
print(e)

"""
filter function

"""
seq=[1,2,3,4,5]
print(list(filter(lambda num:num%2==0,seq)))

"""

"""
s="my name is rochak sharma"
a=s.lower()
b=s.upper()
c=s.split("is")
c1=s.split()
d=s.strip("sharma")
print(a)
print(b)
print(c)   #it creates list from text
print(c1)
print(d)
         

t= "hello i am surya"
print(t)
#t[0] = "M"         # <<< strings are immutable


x = 'Apple'
for y in range (0,5):
    print (x[y], "=", id(x[y]))
                                        #id return memeory location
print(x[0]," memory location ",id(x[0]))

#file reading
fileptr = open("C:/Users/Rochak Sharma/Desktop/controller_projects/ADVANCE_PYTHON/BEGINNERS/1. BASIC_PYTHON_revesion/1. LIST, Tupple,Loop/poem.txt","r")  
print(fileptr)
if fileptr:  
    print("file is opened successfully")  
#print all characters
for num in fileptr:
    print(num)

#add content in file
fileptr = open("poem.txt","a")  
fileptr.write("new data")


#Renaming the file 
 
import os;  
  
#rename file2.txt to file3.txt  
os.rename("poem1.txt","file3.txt") 
os.remove("file3.txt")  
os.mkdir("new")  


#close file
fileptr.close() 



#CREATING A NEWFILE
fileptr = open("file8.txt","x");   
  
print(fileptr)  
  
if fileptr:  
    print("File created successfully");  





























