
"""
Guido van Rossum --> 1980s

python is a simple,
            dynamic programming language where in dynamic language there is no need to specify data type of variable (*NOTE = static programming language where data type of variable is specified ) 
            High level means human readable language (*NOTE =  low level means only machine can understand) 
            interpreted programming language where interpreter scan one line at a time and interprete it (*NOTE = compiler scan all code at a time and compile it) 
            general purpose programming language

inbuilt function --> which are pre-defined function in python
            print() used to print msg/output on screen/console
            type() used to check type of variable
            id() function used to check the memory location

variables are like containers, they are used to store data                        syntax : variable_name = value 
input() function is used to take data from user and store it into variable that is defined by us
"""
name = input("Enter your name ")
print("my name is",name) 

"""
input() function always works on string data type means it always gives string value
if you want to convert one data type into anyother data type , use Data-type casting which convert one data type into another data type
"""
m1 = input("Enter first number: ")
print(type(m1))
m2 = input("Enter second number: ")
print(type(m2))
sum = m1 + m2 
print("sum of two numbers",sum)  

num1 = input("Enter first number: ")
print(type(num1))
num1 = int(num1)
num2 = input("Enter second number: ")
num2 = int(num2)
sum = num1 + num2 
print("sum of two numbers",sum)  
 
#Shortcut method

n1 = int(input("Enter first number: "))             
n2 = int(input("Enter second number: "))
sum = n1 + n2 
print("sum of two numbers",sum)  

#Best method to use

"""
whereas it is kinda troubelsome to convert string data type arrived from input function to another data type
so we can use eval() function which can easily convert data type according user input
"""

A = eval(input("Enter first number: "))             
B = eval(input("Enter second number: "))
sum = A + B
print("sum of two numbers",sum)  

"""
identifiers --> The name which is used for identification purpose that name by default consider as identifier 
                e.g, variable name, function name , class name, method name
                rules --> 
                        1) It can contain alphanumeric character (A-Z,a-z,0-9) 
                        2) It should not start with Digit 
                        3) _ It is only symbol used in identifiers 
                        4) Space not allowed 
                        5) Python identifiers are case sensitive 
                        6) Keywords can not be identifiers 
                        7) There is no length limit to define identifiers

Keywords --> Reserveed word which is having its own meaning 
             python has 35 keywords 
             e.g, def, if, else, del, pass, continue,... 

data type --> Data type are used to define type of variable 
              there are two types of data type...fundamental and collective 
                  1) fundamental data type -->  fundamental data types are also known as primitive or basic data types. 
                        int     used to represent integer value ... int is a data type Which contain Simple numericle or integer value
                        float   used to represent float value ... float is a data type Which contain point Or dot In numeric value
                        complex 
                        string  
                        boolean 
                  2) Collective data type --> are like containers which are used to store multiple values.
                        List   
                        Tuple 
                        set  
                        frozenset 
                        dictionary 
                        range 
                        none 

"""

import keyword 
print(keyword.kwlist)  #To print list of keyword

from keyword import kwlist  
print(kwlist)


"""
Module --> A module in Python is defined as a file containing specific Python statements and definitions.
           A python module contains collections of functions and global variables and also functions inside .py extension file.
           Modules are used to organize code into separate files.
           Python has a large number of built-in modules, and users can create their modules.
      
packeges --> Python packages are directories holding subpackages and modules together.

In Python, a library refers to a collection of modules or packages that contain pre-written code and functionalities.
"""


"""
ADVANTAGES OF PYTHON -->
- Easy to read and write code
- Large standard library with pre-built modules
- Cross-platform compatibility
- Integration with other programming languages




APPLICATION IN PYTHON -->
Web development:
                   Python is used to build web applications and websites.
Data analysis: 
                   Python is used to analyze and manipulate data. Libraries like NumPy, Pandas, and Matplotlib are used for data analysis.

Artificial intelligence and machine learning: 
                   Python is used to build machine learning models and artificial intelligence applications.

Automation:
                    Python is used to automate tasks and processes.
"""
