"""
Decorator --> It is a functon which takes other function as input, and add additional functionalities and return it
"""
# Callng a function from other file
# from 6_encapsulation import Printer

# Printer()

# Using one decorator on one function
#Addition of three numbers using deco
def deco(fun):
    def inner():
        sum = fun()
        c = eval(input("Enter Third number: "))
        sum = sum + c
        return sum
    return inner

@deco
def addition():
    A = eval(input("Enter first number: "))             
    B = eval(input("Enter second number: "))
    sum = A + B
    return sum

# addition = deco(addition)               #Option to @deco
print(addition())


# Using Two decorator on one function
#Printing name and surname in capital
def uppercase(fun):
    def inner():
        full_name = fun()
        full_name = full_name.upper()
        return full_name
    return inner

def splitstring(fun2):
    def inner():
        full_name = fun2()
        full_name = full_name.split()
        return full_name
    return inner

# @splitstring
# @uppercase
def detail():
    f = input("Enter your first name : ")
    s = input("Enter Your surname : ")
    full_name = f + " " + s
    return full_name

detail = uppercase(detail)              #Option to @uppercase
print(detail())

detail = splitstring(detail)            #Option to @splitstring
print(detail())


# Using one decorator on Two function
def decor(fun):
    def inner(*args):
        for i in args[1:]:
            if i == 0:
                return "We can't divide by zero"
        return fun(*args)
    return inner

@decor
def div1(a,b):
    return a/b
print(div1(10,5))

@decor
def div2(a,b,c):
    return a/b/c
print(div2(10,5,0))