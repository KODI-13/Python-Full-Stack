"""
Encapsulation --> Wraping variable and methods in one unit that in class

Public variable --> public variable can be accesseed inside the method
                    public variable can be acceessed and update outside of the class using refernce/object variable
            
(*NOTE = To convert a public variable into private variable we use double underscroe infront of varable)

Private variable --> private variable can be accesseed and update inside the method of same class
                     private variable can't be acceessed and update outside of the class using refernce/object variable
"""
# # Bank Details
# class Bank:
#     def __init__(self,bank_name,branch,name,acc_no,adhaar,balance):     
#         print("hello i am init function or constructor")
#         self.bank_name = bank_name          #variables
#         self.branch = branch
#         self.name = name
#         self.acc = acc_no
#         self.ud = adhaar
#         self.bal = balance

#     def detail(self):                       #method
#         print(f"""hello i am function
#               Bank name = {self.bank_name}
#               Branch = {self.branch }
#               coustmer name = {self.name}
#               Acc no = {self.acc}
#               adhaar = {self.ud}
#               balance = {self.bal }
              
#               """)
        
# s1 = Bank("sbi","chowk","vijay",24241342021, 122334456789,2000)

# s1.detail() 

class Counter:
    counter = 0
    def inc(self):
        self.counter = self.counter + 1
    def dec(self):
        self.counter = self.counter - 1
    def check(self):
        print(self.counter) 

c1 = Counter()
c1.check()
c1.inc()
c1.inc()
c1.inc()
c1.check()
c1.dec()
c1.check()
c1.counter = 500        # public variable can be acceessed and update outside of the class using refernce/object variable
c1.check()

class Counter:
    __counter = 0
    def inc(self):
        self.__counter = self.__counter + 1
    def dec(self):
        self.__counter = self.__counter - 1
    def check(self):
        print(self.__counter) 

c1 = Counter()
c1.check()
c1.inc()
c1.inc()
c1.inc()
c1.check()
c1.dec()
c1.check()
# print(c1.__counter)         # private variable can't be acceessed outside of the class using refernce/object variable
c1.__counter = 500            # private variable can't be update outside of the class using refernce/object variable...it just create a new variable
c1.check()
print(c1.__dict__)            # to check the all coontents/data that a object has




#related to decorator file

def deco(fun):
    def inner():
        fun()
        print("hello in deco")
        print("hello in deco")
        print("hello in deco")
        print("hello in deco")
    return inner

@deco
def Printer():
    print("hello")
    print("hello")

# Printer = deco(Printer)        #Option to @deco
Printer()

