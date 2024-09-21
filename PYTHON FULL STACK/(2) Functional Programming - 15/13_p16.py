#WAP to count number
l = [11,22,334,11,11,22,11,11]
num = int(input("Enter a number you wanna count : "))
count = 0
for i in l:
    if i == num:
        count+=1
print(count)