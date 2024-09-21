# printing local variables inside it function
a = 10
def f1():
    b = 20
    print(b)

    def f2():
        c = 30 
        print(c)

        def f3():
            d = 40 
            print(d)
      
        f3()
        
       
    f2()
    
 
print(a)
f1()


# printing local variables outside of function..i.e in global scope
a = 10
def f1():
    b = 20
    print(b)

    def f2():
        c = 30 
        print(c)

        def f3():
            d = 40 
            print(d)
            return d
        
        d = f3()
        print(d)
        return c 
    
    c = f2()
    print(c)
    return b

print(a)
b = f1()
print(b) 


a = 10
def f1():
    b = 20
    print(b)

    def f2():
        c = 30 
        print(c)
        

        def f3():
            d = 40 
            print(d)
            
        
        
        return f3
    
   
    return f2

print(a)
f2 = f1()
f3 = f2()
f3()


#using all the print's at main global body
a = 10
def f1():
    b = 20
    # print("b")

    def f2():
        c = 30 
        # print("c")
        

        def f3():
            d = 40 
            # print("d")
            return d
            
        
        
        return c,f3
    
   
    return b,f2

print(a)
b,f2 = f1()
print(b)
c, f3 = f2()
print(c)
d = f3() 
print(d)

