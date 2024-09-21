"""
Higher order function --> functon which is getting other function as argument is called as higher order function
                          e.g..pre-built hof in pythons are
                               filter()
                               map()
                               reduce()
"""
# def gr(num):   #TypeError if num varibale is not given : gr() takes 0 positional arguments but 1 was given
#     if num > 10:
#         return num
# gr(12)         #TypeErro if argument is not passed : gr() missing 1 required positional argument: 'num'

l = [1,2,3,44,55,66]
def gr(lit):
    nl = []
    for i in lit:
        if i>10:
            nl.append(i)
    return nl 
nl = gr(l)
print(nl)

"""
syntax :
filtre(fun,seq)              we passing function and sequence in it and filter function filter the sequence according to the logic in passed function
                             mostly we used realtional operators in filter function  (*NOTE = lambda's expression can use any operator)
"""

l = [1,2,44,55,66,12,23]
def gr(num):
    if num > 10:
        return num
f = filter(gr,l)
#print(f)    #<filter object at 0x000001F91833B940>
print(list(f))

l = [1,2,3,44,55,66]
f = filter(lambda num:num>10,l)
print(list(f))


def p(num):
    if num > 0:
        
        return num

sq = p(12)
print(sq)

l = [11,-22,-33,44,-55,66]
def positive(li):
    m = []
    for i in li:
        if i >0:
            m.append(i)
    return m
pos = positive(l)
print(pos)


l = [11,-22,-33,44,-55,66]
def cr(num):
    if num > 0:
        return num
k = filter(cr,l)
#print(f)    #<filter object at 0x000001F91833B940>
print(list(k))


l = [11,-22,-33,44,-55,66]
plus = filter(lambda num: num >0,l)
print(list(plus))

l = [11,22,33,44,55,66]
even = list(filter(lambda num: num%2 == 0,l))
print(even)


a = "G7D82F4"
alpha = []
num = []
for i in a:

    if i.isalpha():
        alpha.append(i)
    else:
        num.append(i)
p = alpha.sort()
k = num.sort()
alpha.extend(num) 
s = ''.join(alpha)
print(s)

