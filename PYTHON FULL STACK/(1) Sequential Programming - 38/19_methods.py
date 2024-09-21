"""
methods in dictionary

key() it returns the list of keys in the dictionary                                syntax:  var_name.keys()
values() it returns the list of values in the dictionary                           syntax:  var_name.values()
items()  it returns the list of tuple of key and values in the dictionary          syntax:  var_name.items()
"""
marks = {"mar":89,"eng":78,"phy":45}
print(marks.keys())
print(marks.values())
print(marks.items())

details = {"name":"raj","city":"pune","age":24}
for i in details:                                       # for loops iterats key in the details dictionary
    print(details[i])

#2nd method
for i in details.values():
    print(i)

print("="*100)
details = {"name":"raj","city":"pune","age":24}
for i in details.items():
    print(i) 

for i,j in details.items():
    print(i)
    print(j)