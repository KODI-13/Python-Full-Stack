"""
Nested function --> function inside function
syntax:
        def f1():
            #body f1
            def f2():
                #body f2
"""
x = 100
def f1():
    y = 200
    print(y)
    def f2():
        z = 300
        print(z)
    f2() 
print(x)
f1() 

x = 100
def f1():
    y = 200
    print(y)
    def f2():
        z = 300
        print(z)
        print(y)
        print(x)
    f2() 
print(x)
f1() 

x = 100
def f1():
    y = 200
    print(y)
    def f2():
        z = 300
        print(z)
        print(y)
        print(x)
    f2() 
    # print(z)        #local scope data can be accessed in the local scope
print(x)
f1() 


x = 100
def f1():
    y = 200
    print(y)
    def f2():
        z = 300
        print(z)
        print(y)
        print(x)
        return z
    z = f2() 
    print(z)        #local scope data can be accessed in the local scope using return keyword
print(x)
f1()

x = 100
def f1():
    y = 200
    print(y)
    def f2():
        z = 300
        print(z)
        print(y)
        print(x)
        return z
    z = f2() 
    print(z)        #local scope data can be accessed in the local scope
    return y
print(x)
y = f1()
print(y)

# returning function from function
x = 100
def f1():
    y = 200
    print(y)
    def f2():
        z = 300
        print(z)
    return f2 
f2 = f1()
f2()

x = 100
def f1():
    y = 200
    print(y)
    def f2():
        z = 300
        print(z)
    return f2,y
f2,y = f1()
f2()
print(y)


x = 100
def f1():
    y = 200
    print(y)
    def f2():
        z = 300
        print(z)
        return z
    return f2,y
f2,y = f1()
z = f2()
print(y)
print(z)

# Difference between two codes (3rd and 4th code for help)
x = 100 
def f1():
    y = 200
    print(y)
    print(x)
    def f2():
        z = 300
        print(z)
        print(x)
        print(y) 
        return z
    z = f2()
    print(z)
    return y,f2
y , f2 = f1()
print("x = ",x)
print(y)
print(f2())
# f2()

x = 100 
def f1():
    y = 200
    print("y = ",y)
    print(x)
    def f2():
        z = 300
        print(z)
        print(x)
        print(y) 
        return z
    z = f2()
    print(z)
    return y,f2
y , f2 = f1()
print("x = ",x)
print(y)
# print(f2())
f2()


x = 100
def f1():
    y = 200
    print("y = ",y)
    def f2():
        z = 300
        print("z = ",z)
        # return z
    return f2
f2 = f1()
print(f2())         #it calls the function and then print returnd value...where if there is nothing to return then it print none
f2()

x = 100
def f1():
    y = 200
    print("y = ",y)
    def f2():
        z = 300
        print("z = ",z)
        return z
    return f2
f2 = f1()
print(f2())
f2()