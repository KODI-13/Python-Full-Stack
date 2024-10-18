"""
string formatting
output function 
print function has two attribute 
1) sep by default its value sep = " " ....separate value written in print
2) end attribute and by default its value is end = "\n" stands fo next line

\t stands for 1 tab
"""
a= 10 
b=20 
print(a,b)

a= 10 
b=20 
print(a,b,sep = "@")
print("hellowelcome",sep = " ")

print("hello\nwelcome")
print("hello welcome")
print("hello\twelcome")

a= 10 
b=20 
print(a,end = "\n")
print(b) 
print(a,end = "")
print(b) 
print(a,end = " ")
print(b) 
print(a,end = "#")
print(b,end = "#") 
print(b)

l =[10,20,30,40,50]
for i in l:
    if i>=30:
        print(i,end = " ")

"""
string formatting --> String formatting in Python allows you to create dynamic strings by combining variables and values.
1) .format() ........ called as dot format method                               syntax : print("msg {} msg {}".format(var1,var2)) ..the curly bracket is called as place holder
2) f"" ............. called as f string                                         syntax : print(f"msg {var1} msg {var2}")

""" 
name = "jay" 
age = 24 
city = "pune" 

print("\n\nmy name is",name,"my age is",age,"i'm from",city)
print("my name is {} i'm {} year old i'm from {}".format(name,age,city))
print("my name is {} i'm {} year old i'm from {}".format(age,name,city)) 
print("my name is {1} i'm {0} year old i'm from {2}".format(age,name,city))                   #using indexing
print("my name is {n} i'm {a} year old i'm from {c}".format(a = age, n = "name", c = city))     #using key and value

nav = "vijay" 
vay = 24 
shahar = "pune" 

print(f"my name is {nav} i'm {vay} year old i'm from {shahar}")
