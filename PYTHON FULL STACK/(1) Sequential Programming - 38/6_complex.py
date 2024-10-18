
c=5+10j                             #format of complex number
print(type(c))                      #Give the type of vaiable
print("Real part =", c.real)        #Give the real part of complex number           
print("imaginary part =", c.imag)   #Give the imaginary part of complex number 

"""
complex number --> it consist of two parts, i.e. real part and imaginary part

1.Real part can be int or float 
         python alwyas convert interger value into decimal value
         ways t0 represent interger are 
         1.binary 
         2.octal 
         3.Decimal 
         4.hexa-decimal 
2.imaginary part must be decimcal or float 

"""


# 1.binary     ----- binary value are 0 and 1 ---represnt 0bvalue ---the value ahead b is binary format
num =1010
print("num =",num)

num1=0b1010
print("num1 =",num1)

n=10
print("Bnary of n =",bin(n))           # bin() this function used to give binary value of number

# 2.octal     -------- octal value are 0 to 7 ---- represent 0ovalue ----- the value ahead o is in octal format
num3=0o123456543
print(num3) 

#num4=0o123459543       #it gives error because value of octal value varies from 0 to 7
#print(num4) 

n1=10
print("Octal of n =",oct(n1))          # oct() this function used to give octal value of number

# 3.Decimal -------- Decimal value are 0 to 9

# 4.hexa-decimal -------- hexa decimal value are 0 to 9 and a-f or A-F ---- represent 0xvalue 
num5=0x10
print(num5)

n3=10
print("Hexa decimal of n3 =",hex(n3))          # hex() this function used to give hexa-decimal value of number


a=0b1010+6j 
print(a) 

b=0o12+7j 
print(b)

c=10+8j
print(c) 

d=0xa+9j
print(d) 