"""
Aim of oop is to implement real word entities (i.e. pillers of oop)

Pillers of oop --> 1) Inheritance
                   2) Polymorphisms
                   3) Encapsulation
                   4) Abstraction

1) Inheritance --> used when One class have to access data of other class
                   Child class is inherit by Parents class
                   (*NOTE = Child class == The class is getting inherit by other class)
                   (*NOTE =  Parents class == The Class which is inheriting other classes)

                   Type of Inheritence --> a) Single Inheritence        = One parent class and one child class (i.e. one class is inherit by only one class)
                                           b) Multi-level Inheritence   = there are multiple classes available but they are serialy inherited (i.e 2nd inherite by 1st and 3rd inherit by 2nd ,4th inherit by 3rd and so on)
                                           C) Multiple Inheritance      = multiple parent class and one child class (i.e. one class is inherit by multile class)
                                           d) Hierachical Inheritance   = single parent class and multiple child class (i.e. multiple class is inherit by one class)
                                           e) Hybrid Inheritence        = Combination of all types of inheritance (i.e.  Simple/Single, Multi-level, Multiple and Hierachical Inheritance  )
"""

# Simple / Single Inheritence
class Parents:
    def property(self):
        print("gold","farm")
p1 = Parents()
p1.property()

class Child(Parents):   #Child class is inherit by Parents class
    # def property(self):
    #     print("gold","farm")
    pass
c1 = Child()
c1.property()

# Multi - level  Inheritence
class P:
    def m1(self):
        print("M1 is method of p")
class C(P):
    def m2(self):
        print("M2 is method of C")
class C_c(C):
    def m3(self):
        print("M3 is method of C_c")

cc = C_c()
cc.m3()
cc.m2()
cc.m1()


# Multiple Inheritance
class P1:
    def m1(self):
        print("M1 is method of p1")
class P2:
    def m2(self):
        print("M2 is method of p2")
class P3:
    def m3(self):
        print("M3 is method of p3")
class C(P1,P2,P3):
    def m4(self):
        print("M4 is method of C")

c1 = C()
c1.m4()
c1.m3()
c1.m2()
c1.m1()


# Hierachical Inheritance 
class Prnt:
    def m1(self):
        print("M1 is method of p1")
class Chld1(Prnt):
    def m2(self):
        print("M2 is method of Chld1")
class Chld2(Prnt):
    def m3(self):
        print("M3 is method of Chld2")
class Chld3(Prnt):
    def m4(self):
        print("M4 is method of Chld3")

c1 = Chld1()
c1.m2()
c1.m1()

s1 = Chld2()
s1.m3()
s1.m1()

ch = Chld3()
ch.m4()
ch.m1()

#Hybrid Inheritance
class Z:
    def p(self):
        print("This is class z")
class A(Z):
    def c(self):
        print("This is child class A of parent Z")
class B(A):
    def c_c1(self):
        print("This is child class B of parent A")
class C(A):
    def c_c2(self):
        print("This is child class C of parent A")
class D(B):
    def c_c1_c(self):
        print("This is child class D of parent B")
class E:
    def P2(self):
        print("This is parent class 2")
class F(C,E):
    def c_c1_c(self):
        print("This is child class F of parent C and E")

a1 =  A()
a1.c()
a1.p() 

b1 = B()
b1.c_c1()
b1.c()
b1.p() 

c1 = C()
c1.c_c2()
c1.c()
c1.p()

d1 = D()
d1.c_c1_c()
d1.c_c1()
d1.c()
d1.p() 

e1 = E()
e1.P2() 

f1 = F() 
f1.c_c1_c()
f1.c_c2()
f1.P2()
f1.c()
f1.p()
