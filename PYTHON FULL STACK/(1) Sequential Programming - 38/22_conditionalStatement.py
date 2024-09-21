"""
flow control statement --> use to control the flow of statement
1) conditional statement
        a) if statement
        b) if else statement
        c) if elif else statement
2) iterative statement
        a) for loop 
        b) while loop
3) transfer statement
        a) pass
        b) continue
        c) break
""" 


"""
a) if statement --- use when we have to put a condition

syntax  ----> 
            if condition:                           where 'if' are keyword...when condtion is true then it enter it's body whether it move forward
                #body_if                                   space after ':' is called as indatation....std value of this indentation is 4 space = 1 tab
                #logic

"""

age = int(input("enter your age : "))
if age>18:
    print("you are eligible for votiong") 
print("hey")

#print number greater than 40
l = [11,22,33,44,55,66] 
for i in l:
    if i>40:
        print(i)

#print negative number
l = [99,-88,77,-66,-999]
for i in l:
    if i<0:
        print(i) 

#print positive number form following set
k = []
s={11,-22,33,-44,55,-66} 
for i in s:
    if i>0:
        k.append(i) 
print(k) 

#print the name whose age is above 18    ...for loop iterates --- dictionary = keys , list = element, string = character
v = {"akshay":27,"amit":23,"dhanshree":14,"mayur":26,"pallavi":15} 
k = []
for i,j in v.items():
    if j >18:
        k.append(i)
print(k)

#2nd method -- shortcut method
v = {"akshay":27,"amit":23,"dhanshree":14,"mayur":26,"pallavi":15} 
k = []
for i in v:
    if v[i] >18:                #we access value
        k.append(i)
print(k) 

#print number divisbile by 4
l = [3,4,12,15,24,9]
for i in l:
    if i%4 == 0:
        print(i)

#print number divisbile by 4  and 3      
l = [3,4,12,15,24,9]

for i in l:
    if i%3 == 0 and i%4 == 0:
        print(i)

"""
b) if else statement --- use when we have two options

syntax  ----> 
            if condition:                           where 'if' is keyword...when condtion is true then it enter if's body body otherwise it enters else body
                #body_if                                   space after ':' is called as indatation....std value of this intendation is 4 space = 1 tab
                #logic
            else: 
                #else_body                           where 'else' is keyword
""" 

per = eval(input("Enter your percentage"))
if per >= 90:
    print("you are eligible for goverment collage") 
else: 
    print("you are eligible for private collage")

num = 24
if num%2 == 0:
    print("it's even number") 
else:
    print("it's odd number")

#wap to print even number from given list 
l = [11,22,33,44,55,66]
for i in l:
    if i%2 == 0:
        print(i)

#wap to print list of even number and list of odd from given list 
l = [11,22,33,44,55,66]
even = []
odd = []
for i in l:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i) 
print(even)
print(odd) 

#wap to print set of positive number and list of nagative number from given list 
l = [11,-22,33,-44,55,-66] 

set = set()
list = []
for i in l:
    if i > 0:
        set.add(i)
    else:
        list.append(i) 
print(set)
print(list) 

#wap to print list of pass student and list of fail student from given dictionary
result = {"mayur":78,"advait":89,"monika":34,"sarang":39}
Pass = []
fail = []
for i in result:
    if result[i] >= 40:
        Pass.append(i)
    else:
        fail.append(i)
print(Pass)
print(fail) 

#wap to print dict of square of even number and dict of square odd from given list
l = [1,2,3,4,5,6,7] 
even = {}
odd = {}
for i in l:
    if i%2 == 0:
        even[i] = i*i 
    else : 
        odd[i] = i*i 
print(even)
print(odd) 

"""
b) if elif else statement --- use when we have to put multiple condition

syntax  ----> 
            if cond1:                  where 'if', 'else' and 'elif' are keyword...
                #body_if                      when condtion is true then it enter if's body otherwise it enters elif body and if both if and elif condition are false then it enters else body
                #logic                        space after ':' is called as indatation....std value of this intendation is 4 space = 1 tab
            elif cond2: 
                #body_elif
            elif cond1: 
                #body_elif
            else: 
                #else_body               
                         
""" 

ajay = 21 
vipul = 22 
amit = 23 

if ajay>vipul and ajay>amit:
    print("ajay")
elif vipul>ajay and vipul>amit:
    print("vipul")
else:
    print("amit")

#calculator 
A = eval(input("Enter first number : "))
opr = input("Enter the opr + , - , * , / ---->")
B = eval(input("Enter second number : ")) 
if opr == "+":
    print(A + B) 
elif opr == "-":
    print(A - B) 
elif opr == "*":
    print(A * B) 
elif opr == "/":
    print(A / B) 
else: 
    print("invalid intput") 


#WAP to print month accordrding to number
mon = eval(input("Enter the month 1 to 12---->"))
if mon == 1:
    print("January") 
elif mon == 2:
    print("Febuary") 
elif mon == 3:
    print("March") 
elif mon == 4:
    print("April") 
elif mon == 5:
    print("May")  
elif mon == 6:
    print("June") 
elif mon == 7:
    print("July")  
elif mon == 8:
    print("August") 
elif mon == 9:
    print("September") 
elif mon == 10:
    print("Octomber") 
elif mon == 11:
    print("November") 
elif mon == 12:
    print("December") 
else: 
    print("invalid input")

#WAP to give grades according to percentage
per  = eval(input("Enter your percentage : "))
if per>= 90:
    print("A+ Grade") 
elif per < 90 and per>=80 :
    print("A Grade") 
elif per < 80 and per>=70: 
    print("B+ prade") 
elif per < 70 and per>=60: 
    print("B Grade") 
elif per <=60: 
    print("C Grade")     
else: 
    print("invalid intput") 

#WAP to compares 4 number
a = eval(input("Enter your number : ")) 
b = eval(input("Enter your number : ")) 
c = eval(input("Enter your number : ")) 
d = eval(input("Enter your number : ")) 
if a>b and a>c and a>d:
    print("a is greater") 
elif b>a and b>c and b>d:
    print("b is Greater") 
elif  c>a and c>b and c>d: 
    print("c is graeter") 
else: 
    print("d is Greater") 

