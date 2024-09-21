#WAP to check a number is Armstrong or not 
num1 = int(input("Enter a number : "))
num2 = str(num1)
n = len(num2)
sum = 0
for i in num2:
    sum = sum + int(i)**n
    if  sum == num1:
        print("it is armstrong")
        break
else :
    print("it is not armstrong number")