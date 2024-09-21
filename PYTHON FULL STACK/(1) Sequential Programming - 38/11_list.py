"""
list is comma separted value in the square bracket          syntax = var_name = [val1,val2,val3,.....]
the value in square bracket is can be of differnt data type
properties -->
                list is ordered (we can used indexing in oredred data ) ,
                mutable ( add or update or delete anything) [*NOTE = all fundamental data types are immutable(can't add or update or delete anything)], 
                hetergeneous collection of element 
                where insertion order are preserverd 
                and duplicates are allowed 
                
""" 
i = [1,2,3,4,5,6]       #oredred(fixed postion)
print(i) 

a = 100                 #(Fundamental) craete a new object at different memory location but does not UPDATE it
print(id(a)) 
a = 200 
print(id(a))  

m = [10,20,30]          #mutable
print(id(m))  
m.append(40)
print(m) 
print(id(m))  


n = [1,20.5,"san",5+10j,True,[1,2,3]]    #Heterogeneous collection
print(n) 
k = [10,10,10]          #duplicates
print(k) 

"""
how to add data / element in list 
append() add data or value into list at end              syntax: var_name.append(value)
insert() add data or value at perticular location        syntax: var_name.insert(index_no , value)
""" 

z = [] 
print(type(z)) 
print(id(z))
z.append(40) 
z.append("siddhi") 
z.append(12.23) 
z.append(True) 
z.append([1,2,3])
print(z) 

y = [11,22,44,55,77] 
y.insert(3,"saibaba") 
print(y) 

"""
how to access data from list 
1)indexing --> used when fetch the single data               syntax: var_name[index_no]
2)slicing --> used when fetch the Multiple data              syntax: var_name[start index : end_index - 1: step value] 
        start index  --->start  (*NOTE = By default 0)
        end_index ----> end_index-1 (*NOTE = By default len(list))
        step value ---> +1 (*NOTE = By default + 1)
                Left to right step value +1 
                right to left step value -1 
""" 

i = [11,22,33,44,55] 
print(i[0]) 

l1 = [] 
l1.append("Deepak") 
l1.append("kamble") 
l1.append([11,22,33]) 
l1.append("panvel") 
print(l1)  
print(l1[0]) 

n1 = l1[2]
print(n1) 
print(n1[1])  

#shortcut method for above 3 lines of code
print(l1[2][1]) 


m = [11,22,33,[1,2,3,4,5,[11,22,33]],44,55]
m[3].append(6)
m[3][5].append(22) 
print(m) 

k = [11,22,33,44,55,66]
print(k[1:7:+2])

print(k[-1:-4:-1]) 
print(k[-2:-7:-2])
 
l= [11,22,33,44,[1,2,3,4],55,66,[6,7,8]] 

print(l[4][1:5:+1]) 
print(l[-4][-2:-5:-2])  

name = "xes" 
print(name[::-1]) 

"""
how to update value 
by using indexing and slicing                  syntax: var_name[index_no] = update_value
""" 

z = [11,22,33,44] 
z[2] = 69 
print(z)  

#how to update multiple values

l = [11,22,33,44,55,66]

l[1:7:2] = 222,444,666          #you can give values in square bracket also
print(l)

"""
how to delete value from list
remove() this function is used to delete data from list                                         syntax: var_name.remove(value)
pop() this function is used to delete last data from list and return deleted value              syntax: var_name.pop() or   syntax: var_name.pop(index_no)
del() this function is used to delete data from list                                            syntax: del var_name[index_no] (*NOTE = syntax: del var_name It delete variable)
clear() this function is used to clear all data from list                                       syntax: var_name.clear() (*NOTE =  It clear list does not delete variable)
""" 

q = [11,22,33,44,[1,2,3,4],55]
q.remove(22)
q[-2].remove(2)
print(q)  
 
l= ["raj", "vijay", [1,2,3,["ajay","sujay"]]] 
#l[2][3].remove("sujay") 
l[-1][-1].remove("sujay")
print(l) 

k = [11,22,33,44] 
print(k.pop())
print(k)

l = [11,"saibaba","raghav",[77,88,99,[1,2,3],110],100,True,90]
print(l.pop(-2)) 

print(l[3].pop()) 
print(l) 

# print(l[3][3].pop(1)) 

l[3][3].remove(2)
print(l)

z = [11,22,33]
del z[1] 
print(z) 
del z 
# print(z)

l = [1,2,3,4] 
m = l 
print(m) 
print(l) 
l.append(44) 
print(l) 
print(m) 

print(id(m)) 
print(id(l))  

o = [1,2,3,4] 
p = o.copy()
print(o) 
print(p) 
o.append(69)
print(o) 
print(p) 
print(id(o)) 
print(id(p))   


"""
Other function
count() it counts frequency of a particular element                                             syntax = var_name.count("value"/value) 
reverse() it reverse the list                                                                   syntax = var_name.reverse() 
sorted() it gives of a single sorted alphabet                                                   syntax = sorted(var_name)
sort()  it gives of a single sorted alphabet..it updates list permanently                       syntax = var_name.sort()
"""     

l = [11,"saibaba","raghav",[77,88,99,[1,2,3],110],100,True,90] 
print(l[3][3].count(2))
l.reverse()
print(l) 

l = [11,22,33,"raj",44] 
print(l) 

l = [11,22,33] 
m = [44,55,66] 
l.extend(m) 
m.extend(l)
print(l)
print(m) 


