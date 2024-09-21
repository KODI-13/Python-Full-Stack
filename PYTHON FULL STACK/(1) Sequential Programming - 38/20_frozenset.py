"""
frozenset = it is comma separted value {}                                     syntax: var_name = frozenset(seq)
        unorderd (unfixed postion so we cant use index number)
        immutable (we can't add and delete the data but can't upadate the data)
        # hetergeneous collection of immutable element (only fundamental elements and tuple and frozen set)
        where insertion order are not preserverd 
        and duplicates are not allowed 
"""  
f = frozenset([11,22,33,44]) 
print(f)

# f = frozenset({23,34,45,[11,22,33]})
print(f)