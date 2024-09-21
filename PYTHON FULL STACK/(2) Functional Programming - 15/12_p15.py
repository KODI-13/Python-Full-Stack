string = input("Enter the string :")
l = string.split()
# print(l)
l1 =[]
for i in l:
    l1.append(i[::-1])
st = " ".join(l1)
print(st)