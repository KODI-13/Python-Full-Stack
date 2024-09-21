"""
inbuild Attributes --> a) __dict__   = give the details of instance varibles and return a dictionary
                       b) __doc__    = It returns the documentation return inside a class
                       c) __module__ = it returns module

Inbuild Functions -->  a) getattr()  = Get a named attribute from an object
                       b) setattr()  = Sets the named attribute on the given object to the specified value.
                       c) delattr()  = Deletes the named attribute from the given object.
                       d) hashattr() = Return whether the object has an attribute with the given name.

"""
class Employee:
    """This is an employee class"""         # __doc__ attributes only return documentation written here (.i.e in between class defination and constructor name)
    def __init__(self,n,r,c,age=21):
        self.name = n
        self.roll = r
        self.city = c 
        age

#nbbuild Attributes   
e1 = Employee("jay",1,"pune")
print(e1.__dict__)
print(e1.__doc__)
print(e1.__module__)

e2 = Employee("ajay",2,"nashik")
print(e2.__dict__)
print(e2.__doc__)
print(e2.__module__)

#Inbuild Functions
e3 = Employee("deepak",69,"Panvel")
print(getattr(e3,"roll"))
print(getattr(e3,"city"))
# print(getattr(e3,age)) 

setattr(e3,"city","Chowk")      # Does not retrun so we can't print it directly
print(e3.__dict__) 

delattr(e3,"roll")              # Does not return so we can't print it directly
print(e3.__dict__)  

print(hasattr(e3,"city"))
print(hasattr(e3,"roll"))       # Returned in boolean form