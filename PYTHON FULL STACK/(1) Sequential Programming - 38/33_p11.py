#WAp to program to check number is perfect ot not
num = int(input("enter a number : "))

l = []    
for i in range(2,num):

    if num%i == 0:
        l.append(i)

sum = 1
for i in l:
    sum = sum + i
    if sum == num:
        print("it is perfect number")
        break
else:
    print("it is not perfect number")
         