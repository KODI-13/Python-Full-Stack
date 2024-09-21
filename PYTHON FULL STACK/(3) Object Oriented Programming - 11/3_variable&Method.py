"""
class class_name:
    variable
        +
     method

There are three types of variable
1) Instance Variable --> The variable which is accessd inside the instance method is called as instance variable
                        These variable are used to define functionality of object
                        These variable are belong to object only that's why called object level variable
                        Separate copy is created for all object
                        Change made to instance variable by one object will not be reflected by other object 

2) Static/class Variable --> The Varible defined inside the class and outside of the method is called as static/class variable (*NOTE = i.e. in between class and method)
                             Common copy is created for all object
                             used because these varible value is same for all object 

3) Local Variable --> The varible which is passed directly when we are calling method
"""

class Student:
    scl_name = "SNP"                            #These varible is called as class/static Variable
    def __init__(self,n,a,c):
        print("hello i am init function or constructor")
        self.name = n                           #these self.variable_name is called as instance variable
        self.age = a
        self.city = c

s1 = Student("vijay",24,"pune") 
s2 = Student("Sujay",24,"pune") 
print(s1.name)
s1.name = "rahul"       #Change made to instance varible by one object will not be reflected by other object
print(s1.name)
print(s2.name)
print(s1.scl_name)
print(s2.scl_name)
Student.scl_name = "SNP VIDYAMANDIR CHOWK"
print(s1.scl_name)
 
"""
Method -->  The function defined inside the class called as method
            use when we have to do some logic on data

There are three types of variable
1) Instance Method --> The method which works on instance or class/static varible (*NOTE = works on means putting some logic on data)
                       These method is specific for all object 
                       The First Parameter of instance method is self

2) Class Method --> The Method which works on class/static varible (*NOTE = works on means putting some logic on data)
                    The First Parameter of class method is cls
                    we can access it using refernece varible or class name (*NOTE = It is prefer to use class name to access class method)
                    @classmethod is a decorator used to convert a method into a class method
                    Decorator is mandatory if we only want to work on class/static variable

3) Static Method --> The Method which wroks on Local variable 
                     @staticMethod is a decorator used to convert a method into a static method
                     Decorator is mandatory if we only want to work on local variable

"""
#Instance Method -- Accsing instance and static/class variable
class Sbi:
    bank = "SBI"
    branch = "chowk"
    def __init__(self,n,c,adh,ac,bal):
        self.name = n
        self.city = c
        self.adhar = adh
        self.account = ac
        self.balance = bal 
    def details(self):
        print(f"""
        \t\t\t\t{Sbi.bank}                  #Accesing class variable inside class
        name = {self.name}
        city = {self.city}
        Adhar = { self.account} \t\t\t Account no. = {self.account}
        balance = {self.balance}  
        """)
    @classmethod
    def bank_details(cls):
        print("The Bank Name is ", cls.bank)
        print("The Branch Name is ", cls.branch)
    @staticmethod
    def avg(n1,n2,n3):
        print((n1+n2+n3)/3)

c1 = Sbi("Ram","Pune",123423142312,129887098978,100000)
c1.details()
print(Sbi.bank)             #Accesing class variable outside of the class 

c1.bank_details()
Sbi.bank_details()
c1.avg(10,20,30)
