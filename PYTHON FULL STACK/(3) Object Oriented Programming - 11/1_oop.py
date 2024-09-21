"""
object oriented programming --> program written in the form of object and class
                                Implementation of real world entities like polymorphisms, inheritance, encapsulation, abstraction
                                in oop everything is consider as object 
                                                                        for e.g num = 100   .... type(num) .... <class 'int'>
                                Every data-type has inbuilt class


object has function and attributes which is bind in class
Example of email
function --> sending email, writting email, draft
attributes --> Subject, To, From are attributes in email
using oop every function related to email will be within a class and we can call class to access that functions
object has function and attributes which is bind in class

oop --> important terms are
            a) class --> it is a blueprint , imaginary entity or a template which is used to construct object
                         it does not require memory
                         one class can have number of object
                         To run class we must create object
                         if we write function inside the class then it is called as method...
                         the method or function having double underscore infront and backside of it then it is called as magic method or special method
                         it called as magic method because it runs automatically without calling
                         syntax :
                                class class_name():                         where class is keyword...class_name first latter must be in capital letter
                                    #class_body 

            b) Object --> it is physical entity 
                          and require memory for exectuion as it is physical entity
                          one class can have number of object
                          one object has only a single reference variable
                            syntax :
                                    ref_variable = class_name():                         
                                           

            c) Reference variable --> use to access the functionality of the object..... here functionality refers to function and variables
                            syntax :   
                                    ref_variable.fucntion              
                                           
"""

class Student:
    pass

s1 = Student()           #s1 is called as object varrible  or refernce variable and we created object here
print(type(s1))         #<class '__main__.Student'>......s1 object is class of student 


s1.name = "jay"
s1.age = 24
s1.city = "pune"

s2 = Student()          #how to construct object
s2.name = "rshul"
s2.age = 25 
s2.city = "nashik"

print(s1.name)         #how to accees functionality of object usinfg refernce variable
print(s2.city)

"""
constructor --> it is a method..which is used to construct the object
                use for ininitializatiion
                constructor name is fix i.e. init
                constructor has first parameter i.e. self
               

class student:
    def __init__(self):          #if we write function inside the class then it is called as method..... init use to construct object in memoory
        pass                     
#self is reference variable use to access functionality within class
#self is also called as object refernce
#self takes memory location of object
        
"""

class Student:
    def __init__(self):
        print("hello i am init function or constructor")
        self.name = "jay"
        self.age = 21
        self.city = "pune"
    def __detail__(self):
        print("hello i am function")

s1 = Student()
print(s1.name)



class Student:
    def __init__(self,n,a,c):
        print("hello i am init function or constructor")
        self.name = n
        self.age = a
        self.city = c
        print(id(self))

s1 = Student("vijay",24,"pune")
print(s1.city)
print(id(s1))
s2 = Student("ram",23,"mumbai")
print(id(s2)) 


class Student:
    def __init__(self):
        print("hello i am init function or constructor")
        self.name = "jay"
        self.age = 21
        self.city = "pune"
    def detail(self):
        print(f"""hello i am function
              name = {self.name}
              age = {self.age}
              city = {self.city}
              
              """)

s1 = Student()
print(s1.name)
s1.detail()


class Student:
    def __init__(self,n,a,c):
        print("hello i am init function or constructor")
        self.name = n
        self.age = a
        self.city = c
        print(id(self))

    def detail(self):
        print(f"""hello i am function
              name = {self.name}
              age = {self.age}
              city = {self.city}
              
              """)


s1 = Student("vijay",24,"pune")
print(s1.city)
s1.detail()

