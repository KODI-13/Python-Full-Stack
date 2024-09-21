"""
lambda function --> nameless function
                    def keyword is not used for function defination..
                    so we defined these using lambda keyword
                    There is no need to write return statement
                    for multiple operations we use tuple
                    reduces code
                    but can't use conditions in it (like if else)

Advantages -->
                    you can instantly create lambda functon and can pass as argument inside other function
                    lambda function are using higher order functions
                    less code
                    nameless function
                    easy to implement

Disadvantages --> 
                    use only for expressions and not for loops and statement
                    provide less readability



syntax: 
        lambda arg:expression

"""
def inc():
    num = 10
    num=num+5
    return num
print(inc())

puc = lambda num = 10:num+5
print(puc())

def square(num):
    num = num**2
    return num
sq=square(5)
print(sq)

square = lambda num : num**2
sq = square(5)
print(sq)
# print(square(5))

multi = lambda x,y:x*y
m1 = eval(input("Enter first number : "))
m2 = eval(input("Enter second number : "))
print(multi(m1,m2))


def f1():
    x = 10
    def f2():
        print("sum3")
        y = 20
        sum = x +y
        return sum
    print("sum")
    
    return f2
f2 = f1()
print("sum2")
sum = f2()
print("sum4")
print(sum)


sum = lambda x=10: lambda y=20 :x+y
sum1 = sum()
answer = sum1()
# print(sum1)
print(answer)


add = lambda x: lambda y : x + y
num1 =add(20)
num2 =num1(20)
print(num2)

s = lambda x = int(input("Enter first number : ")), y = int(input("Enter second number")) : x + y
print(s())




