"""
scope--> In Python, the scope of a variable determines the portion of the program where you can access that specific variable.
         Not every variable can be accessed from any location in a program.

Global scope and Local Scope
Global scope --> The entire space out of the function is called as global scope
                 The variable defined in the global scope/space is called as global scope variable
                 global scope data can be accessed in global scope 
                 global scope data can be accessed in local scope but can't change without permission 
                 permission means using global keyword with the data that we want to access

Local scope --> the entire space inside the function is called as local scope
                The variable defined in the local scope/space is called as local scope variable
                local scope data can be accessed in the local scope
                local scope data can't be accessed in the global scope
                we can access local scope data in global scope using return keyoord
"""

#global scope data can be accessed in global scope
x = 10
y = 20 

def fun1():
    a = 100
    b = 200
    print(a)
    print(b)

print(x)
print(y)

# global scope data can be accessed in local scope but can't change without permission
x = 10
y = 20 
def fun2():
    a = 100
    b = 200
    # x = x +1
    print(x)

fun2() 


x = 10
y = 20 

def fun3():
    a = 100
    b = 200
    global x,y
    x = x +1
    print(x)


print(x)
fun3() 
print(x)
# print(a)          # local scope data can't be accessed in the global scope 

"""
return --> it is a keyword
           use to return data from local scope or function to the outside of function 
           return value are stored in funtion

           multiple values are stroed in the form of tuple
           return statement is last statement of function

           syntax: return var1,var2
""" 

x = 100
def fun1():
    a = 100 
    b = 200
    return a,b
    print(b)        #can't get executed because return is last statement of function
print(fun1())
# print(a)          #it is returned but not get yet here in variable
a,b = fun1()
print(a)
print(a,b)
