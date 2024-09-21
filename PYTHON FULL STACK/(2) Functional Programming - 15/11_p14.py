string = input("Enter the string :")
alpha = []
num = []
for i in string:
    if i.isalpha():
        alpha.append(i)
    else:
        num.append(int(i))
# print(alpha,num)

for i in range(len(alpha)):
    print(alpha[i]*num[i],end="")
   