"""
Argument --> The data pass in function calling is called as argument
parameter --> The data get in function defination is called as parameter

                                def fn(parameter):
                                    pass

                                fn(argument)

There are four types of argument
1) Positional argument --> It is mendatory to maintain the position
                          number of argument == number of parameter

2) Keyword argument --> Data is in form of key and vakue
                        There is no need to maintain the position
                        number of argument == number of parameter
                    
3) Default argument --> The default parameter can be changed by updated argument
                        The value after default values (parameter) must be default values 
4) Arbitary argument
    Positional aribitary argument --> use when we have to pass comma seperated value
                                      also use when we dont know the amount of argument we have to pass (amount = how much)
    def fn(*X)
        pass
    fn(12,23,43,23,12,32)

    Keyword arbitary argument -->  use when we have to pass key and value..i.e relational data  
    def fn(**X)
        pass
    fn(name = "deep ",age = 21,city = "pune")
"""

# Positional argument
name = input("enter your name : ")
age = int(input("Enter your age : "))
city = input("enter your city : ")
def fn(name, age, city):
    print(f"my name is {name},i'm {age} year old and i'm from {city} city")

fn(name,age,city) 


# Keyword argument 

def fn(age, name, city):
    print(f"my name is {name},i'm {age} year old and i'm from {city} city")

fn(name = "deep ", age = 21, city = "pune")


name = input("enter your name : ")                  #from input
age = int(input("Enter your age : "))
city = input("enter your city : ")
def fn(name, age, city):
    print(f"my name is {name},i'm {age} year old and i'm from {city} city")

fn(name = name,age = age,city = city)

# Default argument 
def sbi(name,city,ac,mb,bname="sbi"):
    print(f"""
                         {bname}
        name = {name}
        city = {city}           account = {ac}
        mobile = {mb}

        """)
sbi(name="deep",mb = 7219462215,city = "panvel", ac = 1243123412)
sbi(name="deep",mb = 7219462215,city = "panvel", ac = 1243123412 , bname="cbi")

# Arbitary argument
# (a) Positional aribitary argument

def main(*args):
    print(args)
main(10,20,30,40,50,60)

# Arbitary argument
# (b) Keyword arbitary argument 

def main(**args):
    print(args)
main(a = 10,b = 20,c = 30,d = 40,e = 50)