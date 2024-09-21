"""
Numpy --> Stands for numeric python
          it is a library which works with array
          it has function which works algebra and matrices
          python has list which works like array but list is heterogeneous collection of data and array contains similar type of data
          also list procedure is slow as compared to array and array is 50 times faster than list
          that's wwhy array is important to wrok on data
          so if you have to use array you have to import it from Numpy Library

data science --> computer science branch where data is stored analysed and some value are derived from it 
                 and we use array to make process faster
                 the function neccessary to do data science are written in Numpy library


"""

import numpy as np
# print(numpy.__version__)      # Direct using with numpy module name
print(np.__version__)           # Not lengthy because of as keyword


l = [11,22,33]
print(l)
print(type(l))
# ar = numpy.array(l)           # Direct using with numpy module name
ar = np.array(l)                # Not lengthy because of as keyword
print(ar)

t= (1,2,3,4,5)
print(np.array(t))
"""
numpy has function which name is array
this fucntion creates array in a sequence
array has type --> 0d, 1d , 2d , 3d, 4d
            0d = 
"""
#od
ar = np.array(10)              
print(ar)
print("-"*10)

#1d --> An array that has od arrays as it's elements
ar = np.array([10,20,30,40])              
print(ar)
print("-"*10)

#2d --> An array that has 1d arrays as it's elements
ar = np.array([[1,2,3],[4,5,6],[7,8,9]])              
print(ar)
print("-"*10)

#2d --> An array that has 2d arrays as it's elements
ar = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])              
print(ar)
print("-"*10)

#ndim --> It is used to check diensions of array
ar = np.array(10)              
print(ar.ndim)

ar = np.array([10,20,30,40])              
print(ar.ndim)

ar = np.array([[1,2,3],[4,5,6],[7,8,9]])              
print(ar.ndim)

ar = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])              
print(ar.ndim)

#Indexing
ar = np.array([10,20,30,40])  
print(ar[0])
print(ar[2])
print(ar[0]+ar[2])

ar = np.array([[1,2,3],[4,5,6],[7,8,9]])              
print(ar[0][1])
print(ar[0,1])      # Another way to aceess the elements of array
print(ar[1][2])

ar = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])              
print(ar[0][1][2])

#Slicing
ar = np.array([11,22,33])  
print(ar[1:3])

ar = np.array([[11,22,33],[44,55,66]])  
print(ar[0][0:2])
print(ar[0,0:2])            # correct way

print(ar[1][1:3])
print(ar[1,1:3])


# The way to use slicing 
ar = np.array([[10,20,30],[11,22,33],[44,55,66]]) 
print(ar[0:2][1]) 
print(ar[0:2,1])            # This is a correct way to use slicing
print(ar[0:3,1])   
print(ar[0:3,1:3])   


"""copy() --> Method to copy array
              After use of copy method the update in one array is not followed by other
"""
ar = np.array([[1,2,3],[4,5,6],[7,8,9]])              
ar2 = ar.copy()
print(ar2)
print(ar)

ar[0,0]=100         # After use of copy method the update in one array is not followed by other
print(ar)
print(ar2)

# view() --> method to copy array but change in one array will be followed by other
ar = np.array([[1,2,3],[4,5,6],[7,8,9]])              
ar2 = ar.view()
ar[0,0]=100
print(ar2)
print(ar)


# Using for loop on array
# for loops iterates single array
#for loop on 1d
ar = np.array([10,20,30,40])              
for i in ar:
    print(i)
print("-"*10)

#for loop on 2d
ar = np.array([[1,2,3],[4,5,6],[7,8,9]])   
print(ar)           
for i in ar:
    print(i)
print("-"*10)

#for loop on 2d
ar = np.array([[10,20,30],[11,22,33],[44,55,66]]) 
print(ar)           
for i in ar:
    for j in i:    
        print(j)
print("-"*10)

#for loop on 3d
ar = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) 
print(ar)
for i in ar:
    print(i)         
print("-"*10)

#for loop on 3d
ar = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) 
print(ar)
for i in ar:
    for j in i:
        print(j)         
print("-"*10)

#for loop on 3d
ar = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) 
print(ar)
for i in ar:
    for j in i:
        for k in j:
            print(k)         
print("-"*100)

"""
iterating single elements from array is kinda troublesome so we use a method which is gievn by python to iterate single elements from array
nditer() --> Mainly it is not method/function it is a class
             iterate single elements from array

"""

ar = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) 
for i in np.nditer(ar):
    print(i)
print("-"*10)

a=np.nditer(ar)         # it is a class that's why we can create object of it 
print(a)
for i in a:             # applying for loop on object to iterate single element from object
    print(i)
print("-"*10)


import numpy as np
arr = eval(input("enter array :"))
ay = np.array(arr)
print(ay)