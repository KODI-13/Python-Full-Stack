"""
Abstraction --> The process by which data and function are defined in such way that only eccenstial details can be seen and unceessary implementation are hidden is called abstraction
                Hiding complex implementation details and showing only signatures to users

# How to achieve abstractions
1) Abstract Class --> by using abc module we can create abstract class                                (*How to create abstract class)
                      where abc stands for abstarct base class 
                      abc module contains ABC Class and by using ABC class we can craete abstract method 
                      abstarct class contains abstract method and non-abstarct method(normal method)
                      if implementaion for each class is different then we create abstarct method 
                                                    otherwise
                      if implementaion for each class is same then we create non-abstarct method
                      we can't craete object of abstract class

                      abstract class is a blueprint for other classes
                      it allows you to create a set of method that must be created within any child classes build from abstarct class
                      class contain all abstract methods interface
                      class contains abracts and non abstract moethod is called as abstract class
                      if we want to provide common interfece for different implemntation of component we use abstract class

# HOW to create abstract method
    abstarct methods are method which have no implemntation
    by using @abstarctmethod decorator
    abstarct method does not have body

If we want to inherit a class by a abstract class then it is mendatory to access(write) abstract methods in inherited (child) classs
"""

from abc import ABC,abstractmethod

class Rbi(ABC):
    @abstractmethod
    def min_bal(self):
        pass

    @abstractmethod
    def crop_loan(self):
        pass
    
    @abstractmethod
    def home_loan(self):
        pass

    @abstractmethod
    def ifsc_code(self):
        pass

    def main_branch_city(self):
        print("Pune")

#r1 = Rbi()          #we can't craete object of abstract class ...... TypeError: Can't instantiate abstract class Rbi with abstract methods crop_loan, home_loan, ifsc_code, min_bal

class sbi(Rbi):
    def min_bal(self):
        print("min --> 500")

    def crop_loan(self):
        print("at 8%")

    def home_loan(self):
        print("at 15%")

    def ifsc_code(self):
        print("SBI00032984")


c1= sbi()
c1.min_bal()
c1.crop_loan()
c1.home_loan()
c1.ifsc_code()
c1.main_branch_city()


class Bom(Rbi):
    def min_bal(self):
        print("min --> 500")

    def crop_loan(self):
        print("at 8%")

    def home_loan(self):
        print("at 15%")

    def ifsc_code(self):
        print("BOM00032984")


b1= Bom()
b1.min_bal()
b1.crop_loan()
b1.home_loan()
b1.ifsc_code()
b1.main_branch_city()
