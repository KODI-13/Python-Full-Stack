"""
Types of programming
    1) sequential programming
    2) functional programming
    3) Object oriented programming

2) Functional programming ---> A function is a block of code which only runs when it is called.
                               it has two parts funcation defination and calling ....
                               it is called as user-defined function
                               it does not run the function until we called it
                               we can reuse it
                               code length reduces
                               we can import function from one file to another file

    a) function defination --> syntax :
                                        def fun_name():                         where def is keyword
                                            #fun_body 
    b) function calling --> syntax : 
                                        fun_name()
"""


def sum():
    n1 = eval(input("Enter first number: "))             
    n2 = eval(input("Enter second number: "))
    n3 = eval(input("Enter second number: "))
    summation = n1 + n2 + n3
    print("sum of two numbers",summation)  

def mul():
    n1 = eval(input("Enter first number: "))             
    n2 = eval(input("Enter second number: "))
    multiplication = n1 * n2 
    print("sum of two numbers",multiplication)  

def div():
    n1 = eval(input("Enter first number: "))             
    n2 = eval(input("Enter second number: "))
    divison = n1 / n2 
    print("sum of two numbers", divison)  

div()
mul()
sum()


#WAP to print lenth of given string 

def lenth(): 
    string = input("Enter a name") 
    len = 0
    for i in string:
        len = len + 1
    print(len)
lenth() 

#WAP to print vowels from given string in list
def vowels():
    str =  input("Enter a name") 
    l = [] 
    for i in str:
        if i.lower() in ["a","e","o","u","i"]:
            l.append(i)
    print(l)
vowels()