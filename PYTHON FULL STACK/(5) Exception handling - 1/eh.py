"""
Try and except  --> syntax:
                              try:
                                    \
                                       full program written here 
                                       (*NOTE = The program which may give error is written inside try Block) i.e. the code which will raise exception
                                       but if there is no error occur inside try block then except block will not get executed and finally block will always executed
                                    \
                              except:
                                    \
                                      error handling block
                                      (*NOTE = The program to handle error After it errors) i.e. code to handle exception
                                      but if there is an error occur inside try block then except block will get executed and finally block will always executed
                                      you can use multiple exception block
                                    \
                        OR    except NameError as msg: (*NOTE = when you know the error / exception name)
ig it's better to use   OR    except Exception as msg: (*NOTE = when you don't know the error / exception name)
                              else:
                                    \
                                      it executes when try block executed completely
                                      if error occur then it executes except block and this block is not get executed
                                    \
                              finally:
                                    \
                                     it always get executed
                                    \

try and except block are mandetory
else and finally block are optional
each exception has inbuillt class
raise is the keyword use to raise/generate a error forcefully 
if you want to create exception then you have to create it's(exception) class and you must inherit it with Exception
"""
n1 = eval(input("Enter first number: "))             
n2 = eval(input("Enter second number: "))
try:
    print("y")
    div = n1 / n2
    print("z")
    print("Division of two numbers",div)  
except:
    print("something went wrong")
print("rest of code")



n1 = eval(input("Enter first number: "))             
n2 = eval(input("Enter second number: "))
try:
    div = n1 / n2
except:
    print("something went wrong")
else:
    print("Division of two numbers",div)  
finally:
    print("rest of code")


# except NameError as msg: (*NOTE = when you know the error / exception name)
n1 = eval(input("Enter first number: "))             
n2 = eval(input("Enter second number: "))
try:
    div = n1 / n2
    # print("Division of two numbers",di)                     # This error is for practice ... don't write it as correct ... and remove comment line while running this program
except ZeroDivisionError as msg:
    print(msg)
except NameError as msg:
    print(msg)


# except Exception as msg: (*NOTE = when you don't know the error / exception name)
n1 = eval(input("Enter first number: "))             
n2 = eval(input("Enter second number: "))
try:
    div = n1 / n2
    # print("Division of two numbers",di)                     # This error is for practice ... don't write it as correct ... and remove comment line while running this program
except Exception as msg:
    print(msg)



age = int(input("enter your age: "))
try:
    if age<0:
        raise ValueError()
except ValueError: 
    print("Age can't be negative")
else:
    print("my age is", age)


# how to create exception
class DivisionByfiveError(Exception):
    pass

n1 = eval(input("Enter first number: "))             
n2 = eval(input("Enter second number: "))
try:
    div = n1 / n2
    if n2 == 5:
        raise DivisionByfiveError()
except DivisionByfiveError :
    print("You can't divide by five cause it is set by us")
else:
    print("The Divisiin is" ,div)