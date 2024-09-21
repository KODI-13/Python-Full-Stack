"""
dictionary =   {}                                                      syntax: var_name = {key1:value1,key2:value2}
        orderd (fixed postion but cant use index number)
        mutable (we can add, delete and upadate the data)
        hetergeneous collection of element 
        data represent in the form of key and value        where key is unique(we can't use it again) and immutable value(immutable data type)
                                                                 value can be dublicate and mutable/immutable

realational type of data stored in deictionary data type

"""  


"""
how to access data from dictonary
we are going to use key                      syntax: var_name[key]                                  

""" 

d = {"name":"deepak","age":21,"city":"pune","marks":99}
print(d["name"])
print(d["age"])
print(d["city"])
print(d["marks"]) 

"""
how to add data / element in dictionary 
we are going to use key                      syntax: var_name[key] = value                       
""" 
d["crush"] = "siddhi"
d["her city"] = "pune"
print(d)

d = {1:{"name":"deepak","age":21,"city":"pune","marks":99},
     2:{"name":"siddhi","age":19,"city":"pune","marks":90}} 
print(d[2])
print(d[1])
print(d[2]["name"])
print(d[1]["city"]) 

d3 = {"name":"janvi","age":16,"city":"pune","marks":98}
d[3] = d3
print(d) 


d[1]["percentage"] = 100
print(d) 

d[2]["percentage"] = 99
print(d) 

d[3]["percentage"] = 91
print(d) 


#emply

square = {} 

for i in range(11):
    n = i **2
    square[i] = n 
    # square[i] = i*i
print(square)

odd = {} 
for i in range(11,51,2):
    odd[i] = i*i

print(odd)


"""
how to update data from dictonary
we are going to use key                      syntax: var_name[key] = update value                               
""" 
d = {"name":"deepak","age":21,"city":"pune","marks":99}
d["name"] = "deep"
print(d) 

student__details = {1:{"name":"deep","age":21,"city":"pune","marks":{"s1":99,"s2":99.09,"s3":99.99}}}
student__details[1]["name"] = "deepak"
print(student__details)

student__details[1]["marks"]["s2"] = 85
print(student__details) 

"""
how to delete data from dictonary
del() this function is used to delete data from dictionary                   syntax: del var_name[key]                              
""" 
details = {"name":"jay","age":23}
del details["age"] 
print(details) 

student__details = {1:{"name":"deep","age":21,"city":"pune","marks":{"s1":99,"s2":99.09,"s3":99.99}}}
del student__details[1]["name"]
del student__details[1]["marks"]["s2"]
print(student__details)


"""
when we try to access the key that is not present in the dictionary then it will show us an error
"""
# print(student__details[1]["marks"]["s2"])             # it will generate error

"""
to handle that error we use get() method
Using get() method (returns None if key is not present)
"""
print(student__details[1]["marks"].get("s2"))


print("="*100)

student = {1:{"name":"deep","age":21,"city":"pune","marks":{"s1":99,"s2":99.09,"s3":99.99}}}
del student[1]["name"]

# using del if you are trying to delete a key that is not present in dictionary then it will show error
# del student[1]["name"]

# To handle it we use pop() method which returns none if key is not present in dictionary (*NOTE = we have to set value equal to None)
print(student[1].pop("name",None))
print(student[1].pop("age",None))


print(student)