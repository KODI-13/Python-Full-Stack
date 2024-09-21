"""
Dictionary comprehension --> comprehension means compacting (compacting means reducing)
                             use when we have to create a new dictionary from a sequence

syntax with for loop -->
                New dictionary = {K:V for tem_variable in sequence}                         (i.e. K = key expression and V = value expression)

syntax with for loop and if condition -->
                New dictionary = {K:V for tem_variable in sequence if condition}            (i.e. K = key expression and V = value expression)

syntax with for loop and if else condition -->
                New dictionary = {K:V if condition else V for tem_variable in sequence}     (i.e. K = key expression and V = value expression)
            
dictionary comprehension does not have if elif else condition
and there is no tuple comprehension like concept
"""
#printing squre of all number
l =[1,2,3,4]            # The sequence here is a list that means you can pass any sequence data-type
d = {}
print(type(d))
for i in l:
    d[i] = i**2      
print(d)

# dictionary comprehension with for loop
# Using dictionary comprehension printing squre of all number
l={1,2,3,4}
nl={i:i**2 for i in l}
print(nl)

#printing squre of even number
l ={1,2,3,4}
d = {}
for i in l:
    if i%2 == 0:
        d[i] = i**2        
print(d)

# dictionary comprehension with for loop and if condition 
# Using dictionary comprehension
l={1,2,3,4}
nl={i:i**2 for i in l if i%2 == 0}
print(nl)

#printing squre of even number and cube of odd numbers
l ={1,2,3,4}
d = {}
for i in l:
    if i%2 == 0:
        d[i] = i**2  
    else:
        d[i] = i**3      
print(d)

# dictionary comprehension with for loop and if else condition 
# Using dictionary comprehension
l={1,2,3,4}
nl={i:i**2  if i%2==0 else i**3 for i in l}
print(nl)