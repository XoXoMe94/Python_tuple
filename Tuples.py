# -*- coding: utf-8 -*-
"""


@author: sara
"""

# Tuples are like list use ()

a=('sara','Alex')
print(a[0]) #sara
print(a)  #('sara', 'Alex')
print(max(a))  #sara



#ex
(x,y)=(1,'fred')
print(x)  #1
print(y)  #fred



#ex
(1,2,3) < (2,3,4)    #true



#ex sort a dic by key
a={'a':1,'c':3,'b':6}
sorted(a.items())  #[('a', 1), ('b', 6), ('c', 3)]
for k,v in sorted(a.items()) :
    print(k,v)  #a  1 
                #b   6
                #c   3
  
#ex sort a dic by value
a={'a':7,'c':3,'b':6}
tmp=list()
for k,v in a.items():
    tmp.append((k,v)) #like a tuple
print(tmp)  #[('a', 7), ('c', 3), ('b', 6)]
tmp=sorted(tmp, reverse=True) 
print(tmp) #[('c', 3), ('b', 6), ('a', 7)]



#ex
fhand=open(r'C:\Users\sara\Desktop\office 2021\sara2.txt')
count=dict()
for line in fhand:
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1
lst=list()
for key,value in count.items() :
    newtup=(value, key)      
    lst.append(newtup)
lst=sorted(lst,reverse=True)

for value,key in lst[:5] : #top5
     print(key,value)    #From 3
                         #2020 2
                         #sara@yahoo 1
                         #Sat 1
                         #Sara 1
              

