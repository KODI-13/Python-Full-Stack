"""
Set = it is comma separted value {}                           syntax: var_name = {val1,val2,val3,.....} 
        Data type of empty set / curly bracket is dictionary 
        to create empty set                                   syntax: var_name = set(sequence) (*NOTE-where sequence means where we can store multiple values include list, tuple, set, dict, string)
"""

s = {1,2,3,4}
print(type(s)) 
m = {}
print(type(m))

l = set()               #it is function where we pass values which return a set .... this function is called as constructor
print(type(l))
print(l) 
v = set("deepak")       #passing string sequence   (it sort the string)
x = set([1,2,3])        #passing list sequence
y = set((4,5,6))        #passing tuple sequence
z = set({7,8,9})        #passing set sequence
print(v)
print(x) 
print(y)
print(z)




m = set([1,2,3,4])
print(m)  

"""
Set = it is comma separted value {}                                     syntax: var_name = {val1,val2,val3,.....}
        unorderd (unfixed postion so we cant use index number)
        mutable (we can add and delete the data but can't upadate the data)
        hetergeneous collection of immutable element (only fundamental elements and tuple and frozen set)
        where insertion order are not preserverd 
        and duplicates are not allowed 
"""  

s = {11,2,30,4}         #unorderd  
print(s) 

n = {1,2,3,4}           #mutable
print(id(n)) 
n.add(70)
print(n) 
print(id(n))

j = {10, 20.3, "san", 9+10j, True, (1,2,3)}            #hetergeneous collection of immutable element (*NOTE = list, set can't be used)
print(j) 

d = {1,20,3,4}           #where insertion order are not preserverd 
d.add(70)
print(d) 

f = {10,2,10,3,4,10}    #duplicates are not allowed 
print(f) 

"""
how to add data / element in set 
add() add data or value into set              syntax: var_name.add(value)
""" 

u = {1,2,3,4}           
u.add(70) 
print(u)
 
"""
how to delete value from set
remove() this function is used to delete data from set                                          syntax: var_name.remove(value)
pop() this function is used to delete any/random data from set and return deleted value         syntax: var_name.pop()
del() this function is used to delete set vaiable                                               syntax: del var_name It delete variable
clear() this function is used to clear all data from set                                        syntax: var_name.clear() (*NOTE =  It clear set does not delete variable)
discard() this function is used to delete data from set                                         syntax: var_name.remove(value)
""" 

m = {10,20,30,40} 
m.remove(40)
print(m) 

z = {10,20,30,40} 
print(z.pop())                  #return deleted value
print(z) 

k = {1,2,3,4}
del k 
# print(k) 

f = {1,2,3,4} 
f.clear()
print(f)
print(type(f)) 

#The differnece beetween remove() and discard() function 
q = {10,20,30,40} 
q.discard(99)                    #it will NOT show error if removed value is not present in set
print(q)

p = {10,20,30,40} 
# p.remove(89)                   #it will show error if removed value is not present in set
print(p) 

v = {10,20,30,30,20,10}          #duplicates are not allowed
print(len(v)) 

"""
Other function
intersection() it gives common values between two sets                                            syntax = var1.intersection(var2) 
difference() it compare two varible and give difference                                           syntax = var1.difference(var2)   (*NOTE =it gives output on var1 w.r.t.o var2)
"""
s = {11,22,33,44}
r = {33,44,55,66}
print(s.intersection(r))        #output = 33,44
print(s.difference(r))          #output = 11,22
print(r.difference(s))          #output = 55,66 

"""
how to access data from Set
we use for loop to aceess data from set                                                        
syntax  ----> 
        for temp_var in sequence:                              where 'for' and 'in' are keyword
                #body for loop                                  space after ':' is called as intendation....std value of this intendation is 4 space = 1 tab
                #statement1
                #statement2

we use for loop to do iterations 
anything wriiten in body will get execcuted until the element in sequence is used 
""" 

l = [11,22,33,44]
for i in l:
    print(i)

t = (11,"deepak",2.3,True,5+10j) 
for j in t: 
    print(j) 

d = "deepak"
for j in d: 
    print(j) 

s = {11,2.4,"yo",False,(11,22,33)} 
for l in s:
    print(l)