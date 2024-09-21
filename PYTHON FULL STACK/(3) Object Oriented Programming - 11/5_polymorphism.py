"""
Polymorphisms --> The word polymorphism means having many forms. 
                  In programming, polymorphism means the same function name (but different signatures) being used for different types. 

Type of Polymorphisms  --> 1) Overloading = within one class
                                            use when we want to redefine(*NOTE = redefine means the changes made according our choice)
                                            
                                            types of overloading --> a) operator overlaoding
                                                                     b) Method overloading (*NOTE = Method overloading is not neccessary in python because python is dynaming langauge where there is no need to define data type of variable )

                           2) Overriding = Within two diff. class
                                           To do overridng it is neccessary that child class is inherit by parent class 
                                           types of overloading --> a) method overriding = redefining paraent class method into child class 
                                                                    b) variable overrriding = redefining paraent class vaiable into child class
"""
# operator overlaoding
"""
in built methods for operators
Addition        = __add__()
Greater than    = __gt__()
Less than       = __lt__()
Division        = __diiv__()
Multiplicatioon = __mul__()
Substractioon   = __sub__()
"""
class Book:
    def __init__(self,name,pages):
        self.name = name
        self.pages = pages 

b1 = Book("xyz",200)
b2 = Book("abc",100)
print(b1.pages+b2.pages)
# print(b1+b2)                    #TypeError: unsupported operand type(s) for +: 'Book' and 'Book'

class Book:
    def __init__(self,name,pages):
        self.name = name
        self.pages = pages 
    def __add__(self,other):
        return self.pages + other.pages

b1 = Book("xyz",200)
b2 = Book("abc",100)
print(b1.pages+b2.pages)
print(b1+b2)      

# Method overloading
# *NOTE = Method overloading is not neccessary in python because python is dynaming langauge where there is no need to define data type of variable 


# Overriding
# a) method overriding
class Parents:
    def property(self):
        print("gold","farm")
    def marry(self):
        print("with janhvi")
p1 = Parents()
p1.property()

class Child(Parents):   
    def property_child(self):
        print("bike","flat")
    def marry(self):
        print("marry sidhhi")
c1 = Child()
c1.property_child()
c1.marry() 

# b) variable overrriding 

class Parents:
    course = "java"
    def property(self):
        pass
p1 = Parents()


class Child(Parents):   #Child class is inherit by Parents class
    def property(self):
        pass
c1 = Child()
print(c1.course) 



class Parents:
    course = "java"
    def property(self):
        pass
p1 = Parents()


class Child(Parents):   #Child class is inherit by Parents class
    course = "python"
    def property(self):
        pass
c1 = Child()
print(c1.course)