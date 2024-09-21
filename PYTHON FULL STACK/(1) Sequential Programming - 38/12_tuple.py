"""
Tuple = it is comma separted value                          syntax: var_name = (val1,val2,val3,.....)
        orderd 
        immutable 
        hetergeneous collection of element 
        where insertion order are preserverd 
        and duplicates are allowed 
""" 
t = (11,22,33)
#t[0] = 33                  its immutable because can't change anything
print(t)

"""
how to access data from tuple
1)indexing --> used when fetch the single data               syntax: var_name[index_no]
2)slicing --> used when fetch the Multiple data              syntax: var_name[start index : end_index - 1: step value] 
        start index  --->start  (*NOTE = By default 0)
        end_index ----> end_index-1 (*NOTE = By default len(list))
        step value ---> +1 (*NOTE = By default + 1)
                Left to right step value +1 
                right to left step value -1  

""" 


t = (11,22,33,44,5,6,9)
n = t[0] 
p = t[4]

k = n**2 + p**2
print(k) 

t = (11,22,33,44,55) 
print(t[0::2])


"""
Diffrence between list and tuple
            List                                            Tuple
        Comma sep.[]                                    comma sep. () 
        '[]' mendatory                                  '()' not mendatory 
        mutable                                         Imutable 
        it required more memory                         it required less memory 
        excution is slow                                exectuion is fast 
        less efficient in memory utilization            more efficient in memory utilization
        unpacking                                       both(packing and unpacking) 
        used when data is unfixed                       used when you have to do fast execution on fixed data
"""

l = [11,22,33]          #'[]' mendatory
print(type(l)) 
l = 11,22,33 
print(type(l)) 

t = (11,22,33)          #'()' not mendatory
print(type(t)) 
t = 11,22,33 
print(type(t))  

o  = (11)               #'()' not mendatory
print(type(o))          #(*NOTE--> Data type is int)

o  = (11,)              #'()' not mendatory
print(o) 
print(type(o)) 

import sys   
l = [11,22,33]              #it required more memory
print(sys.getsizeof(l))

t = (11,22,33)              #it required less memory
print(sys.getsizeof(t)) 



l = [11,22,33,4]            #less efficient in memory utilization 
print(id(l)) 
m = [11,22,33,4] 
print(id(m)) 

t = (11,22,33,4)            #more efficient in memory utilization
print(id(t)) 
k = (11,22,33,4) 
print(id(k))  


l = [11,22,33,44]           
a,b,c,d = l                 #unpacking
print(a)
print(b)
print(c) 
print(d) 
 
l = (11,22,33,44)           
a,b,c,d = l                 #unpacking
print(a)
print(b)
print(c) 
print(d) 

a = 12
b = 23 
c = 34 
d = 45
z = a,b,c,d             #packing
print(z)

print("="*100)
# concatenated 
t1 = (1,2,3)
t2 = (4,5,6)
print(t1 + t2)

# concatenated 
l1 = [1,2,3]
l2 = [4,5,6]
print(l1 + l2)
















print("="*100)
"""
The += operation modifies the original_list
"""
original_list = [1, 2, 3]
print("Original List:", original_list)

modified_list = original_list
modified_list += [4, 5]
print("Modified List:", modified_list)

# Check the original list
print("Original List After Modification:", original_list)


"""
The += operation does not modifies the original_tuple...it creates a new tuple 
"""
original_tuple = (1, 2, 3)
print("Original Tuple:", original_tuple)

modified_tuple = original_tuple
modified_tuple += (4, 5)
print("Modified Tuple:", modified_tuple)

# Check the original tuple
print("Original Tuple After Modification:", original_tuple)
