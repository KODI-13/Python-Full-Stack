"""
Reduce --> Higher order function (functon which is getting other function as argument is called as higher order function)
           reduce the sequence into single value 
"""
from functools import reduce

l = [1,2,3,4]
def add(l):
    sum = 0
    for i in l:
        sum = sum + i 
    return sum
li = add(l)
print(li) 

l = [1,2,3,4]
a = reduce(lambda x,y : x+y,l)
print(a)



