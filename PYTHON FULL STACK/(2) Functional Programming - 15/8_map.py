"""
Map --> Higher order function (functon which is getting other function as argument is called as higher order function)
        It takes sequence also as Argument
        Used when we have to work on each number (i.e dealt with each every number)
"""

def inc(num):
    return num+2
p = inc(11)
print(p)

l = [11,22,33,44,55,66]
def add(l):
    l1 = []
    for i in l:
        i = i+2
        l1.append(i)
    return l1
k = add(l)
print(k)

l = [11,22,33,44,55,66]
def inc(num):
    return num+2
m = map(inc,l)
print(list(m))

l = [11,22,33,44,55,66]
z = map(lambda num:num+2,l)
print(list(z))


num = [1,2,3,4,5,7,8,9,10]
sq = map(lambda n:n**2,num)
print(list(sq))


result = {"math":80,"mar":78,"hindi":85}

a = map(lambda n:result[n]+5,result)
print(list(a))  


result = {"akshay":89,"advat":39,"komal":38,"manish":90}

j = dict(map(lambda x :(x,result[x]+5),result))
print(j)
