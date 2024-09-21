"""
set comprehension --> comprehension means compacting (compacting means reducing)
                       use when we have to create a new set from a sequence

syntax with for loop -->
                New set = {expression for tem_variable in sequence}

syntax with for loop and if condition -->
                New set = {expression for tem_variable in sequence if condition}

syntax with for loop and if else condition -->
                New set = {expression if condition else expression for tem_variable in sequence}
            
set comprehension does not have if elif else condition
and there is no tuple comprehension like concept
"""
#printing squre of all number
l =[1,2,3,4]            # The sequence here is a list that means you can pass any sequence data-type
nl = set()
print(type(nl))
for i in l:
    nl.add(i**2)       
print(nl)

# set comprehension with for loop
# Using set comprehension printing squre of all number
l={1,2,3,4}
nl={i**2 for i in l}
print(nl)

#printing squre of even number
l ={1,2,3,4}
nl = set()
for i in l:
    if i%2 == 0:
        nl.add(i**2)         
print(nl)

# set comprehension with for loop and if condition 
# Using set comprehension
l={1,2,3,4}
nl={i**2 for i in l if i%2 == 0}
print(nl)

#printing squre of even number and cube of odd numbers
l ={1,2,3,4}
nl = set()
for i in l:
    if i%2 == 0:
        nl.add(i**2)  
    else:
        nl.add(i**3)      
print(nl)

# set comprehension with for loop and if else condition 
# Using set comprehension
l={1,2,3,4}
nl={i**2  if i%2==0 else i**3 for i in l}
print(nl)