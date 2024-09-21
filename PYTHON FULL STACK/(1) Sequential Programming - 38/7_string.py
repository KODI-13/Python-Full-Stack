
"""
string = Anything written in single coat ' ' or double coat " "           syntax: var_name = "value"
    but where in java anything written in single coat ' ' is represent as character data type and  anything written in double coat " " is represent as string data type
    python does not have any character data type (i.e. char )
"""

name = "Deepak"
print(name)

"""
how to access element from string 
1. Indexing
 we use indexing to access single element in string
 indexing can be positive(forwared) or negative(reverse) 
 syntax of indexing is var_name[index number]

2. slicing
 we use slicing to access a particular part or mulitple element in string
 by default, search in slicing is from left to rights
 syntax of slicing is var_name[stat index: end index - 1]
 where start index value is optional, its default value set to be 0
 where end index value is optional, its default value is length of string
 when positive(forward) or negative(reverse) slicing is from higher number to lower number then it gives empty value

"""

name = "rameshwaram"
print(name[4])  

print(name[0:6]) 

print(name[-11:-8]) 

print(name[5:20])

print(name[9:1])            #empty slicing

print(name[-1:-5])          #empty slicing 


"""
Function of string
upper() = it convert string into upper case                                                 syntax = var_name.upper()
lower() = it convert string into lower case                                                 syntax = var_name.lower()
title() = it convert first letter of entire string into upper case                          syntax = var_name.title()
capitalize() = it convert first letter of first word of entire string into upper case       syntax = var_name.capetalize()
""" 

name = "the kiran acedemy" 
cls = name[4:9] 
print(cls.upper()) 

print(name[-7:].title()) 
print('-'*10)
print(name[:].title())                  #differ5nce between title and capitalize           
print(name[:].capitalize()) 

# print(name[:]) 

# print (name[:9])


# # You can use the isinstance() function to check if a variable is of a specific type. 
my_variable = 87
# my_variable = "bvgjh"
is_string = isinstance(my_variable, str)
print(is_string)

print(dir(str))    # give all function and method related to it