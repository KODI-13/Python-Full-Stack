"""
flow control statement --> use to control the flow of statement
1) conditional statement
        a) if statement
        b) if else statement
        c) if elif else statement
2) iterative statement
        a) for loop 
        b) while loop
        c) while True
3) transfer statement
        a) pass
        b) continue
        c) break
""" 

"""
a) for loop
we use for loop to aceess data from sequence(i.e. list, tuple, set, dictionary)                                                        
syntax  ----> 
        for temp_var in sequence:                              where 'for' and 'in' are keyword
                #body for loop                                       space after ':' is called as intendation....std value of this intendation is 4 space = 1 tab
                #statement1
                #statement2

we use for loop to do iterations 
anything wriiten in body will get execcuted until the element in sequence is used 

b) while loop -- icu( i = initiailization, c = condition, u = update)
syntax  ----> 
                initiailization                                     where 'while' is keyword
                while condition:                                           space after ':' is called as intendation....std value of this intendation is 4 space = 1 tab
                        #while_body
                        #increment or decrment
we use while loop to do iterations 
anything wriiten in body will get execcuted until the condition is false
"""

num = 10
while num<21:
    print(num)
    num = num + 1 

#wap to print even numbers form 11 to 20
i = 12
while i <21:
    print(i)
    i = i + 2 

#wap to print even numbers form 20 to 11
i = 20
while i>11:
    print(i)
    i = i - 2 

#wap to print list of odd numbers form 45 to 33
i = 43
odd = []
while i>33:
    odd.append(i)
    i = i - 2
print(odd)

#2nd method
i = 43
odd = []
while i>33:
    if i %2 != 0:
         odd.append(i)
    i = i - 2
print(odd) 
 
#wap to print a 6 times hello world
i = 1
while i<=6:
    print("hello")
    i = i + 1

#wap to print a table of number 12
i = 12 
while i <= 120:
    print(i) 
    i = i + 12

#wap to print a table of number 15
i = 1
while i <= 10:
    j= i*15
    print(j) 
    i = i + 1

#wap to print a table of number 15
i = 1
while i <= 10:
    print("15 *", i, "=" , 15*i) 
    i = i + 1

#wap to print a table of number 15
i = 1
while i <= 10:
    print("20 *", i, "=" , 20*i) 
    i = i + 1

#wap to print a table of any number 
i = 1
num  = int(input("Enter a number :"))
while i <= 10:
    print(num ,"*", i, "=" , num*i) 
    i = i + 1

"""
while True -- > to run a loop continuosly 
syntax  ----> 
                while True:                                          where 'while' is keyword ... space after ':' is called as intendation....std value of this intendation is 4 space = 1 tab
                    #while_body

"""
while True:
    A = eval(input("Enter first number : "))
    opr = input("Enter the opr + , - , * , / , % ---->")
    B = eval(input("Enter second number : ")) 
    if opr == "+":
        print(A + B) 
    elif opr == "-":
        print(A - B) 
    elif opr == "*":
        print(A * B) 
    elif opr == "/":
        print(A / B) 
    elif opr == "%":
        print(A%B)
    else: 
        print("invalid intput") 
    ch = input("do you want to continue (y/n) : ")
    if ch == "n" or "N":
        break 

#2nd method
while True:
    A = eval(input("Enter first number : "))
    opr = input("Enter the opr + , - , * , / , % ---->")
    B = eval(input("Enter second number : ")) 
    if opr == "+":
        print(A + B) 
    elif opr == "-":
        print(A - B) 
    elif opr == "*":
        print(A * B) 
    elif opr == "/":
        print(A / B) 
    elif opr == "%":
        print(A%B)
    else: 
        print("invalid intput") 
    ch = input("do you want to continue (y/n) : ").lower()
    if ch == "n":
        break 
