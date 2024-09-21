"""
List comprehension --> comprehension means compacting (compacting means reducing)
                       use when we have to create a new list from a sequence

syntax with for loop -->
                New list = [expression for tem_variable in sequence]

syntax with for loop and if condition -->
                New list = [expression for tem_variable in sequence if condition]

syntax with for loop and if else condition -->
                New list = [expression if condition else expression for tem_variable in sequence ]
            
list comprehension does not have if elif else condition
and there is no tuple comprehension like concept
"""
#printing squre of all number
l ={1,2,3,4}             # The sequence here is a set that means you can pass any sequence data-type
print(type(l))
nl = []
for i in l:
    # i = i**2
    # nl.append(i)
    nl.append(i**2)         # Shortcut for above two step
print(nl)

# list comprehension with for loop
# Using list comprehension printing squre of all number
l=[1,2,3,4]
nl=[i**2 for i in l]
print(nl)

#printing squre of even number
l =[1,2,3,4]
nl = []
for i in l:
    if i%2 == 0:
        nl.append(i**2)        
print(nl)

# list comprehension with for loop and if condition 
# Using list comprehension
l=[1,2,3,4]
nl=[i**2 for i in l if i%2 == 0]
print(nl)

#printing squre of even number and cube of odd numbers
l =[1,2,3,4]
nl = []
for i in l:
    if i%2 == 0:
        nl.append(i**2)  
    else:
        nl.append(i**3)      
print(nl)

# list comprehension with for loop and if else condition 
# Using list comprehension
l=[1,2,3,4]
nl=[i**2  if i%2==0 else i**3 for i in l]
print(nl)