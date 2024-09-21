""" 
function of string
len() function is to give the length of string and length is start from 1                       syntax = len(var_name)
index() it gives index number of particular element, it only gives positive index number        syntax = var_name.index("value")
count() it counts frequency of a particular element                                             syntax = var_name.count("value")
isalpha() it gives True when string contain only alphabates                                     syntax = var_name.isalpha()
isnumeric() it gives True when string contain only number                                       syntax = var_name.isnumeric()
isalnum() it gives True whether string contain alphabates OR number and gives false on symbol   syntax = var_name.isalnum()
istitle() it gives True when string in title format                                             syntax = var_name.istitle()
split() it split entire string                                                                  syntax = var_name.spilt()
sorted() it gives of a single sorted alphabet                                                   syntax = sorted(var_name)
It does not have sort function
replace() it replace one word or letter into another word or letter                             syntax =var_name.replace("old_name","new_name")
"""

name = "rameshwaram2"
print(len(name))
print(name.index("h")) 
print(name.count("a"))
print(name.isalpha()) 
print(name.isnumeric()) 
print(name.isalnum()) 

A = "The Kiran Academy"
print(A.istitle()) 
print(A.split())
print(sorted(A)) 
print(A.replace("Kiran","Deepak")) 

a = "The Kiran acadmey"
print(sorted(a))
# print(sort(a))           # NameError: name 'sort' is not defined. Did you mean: 'sorted'?