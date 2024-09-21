#wap to check if number is prime or not
num = int(input("Enter a number : "))
for i in range(2,num):
    if num%i == 0:
        print("it is not prime number")
        break
else:
    print("it is prime number")
   