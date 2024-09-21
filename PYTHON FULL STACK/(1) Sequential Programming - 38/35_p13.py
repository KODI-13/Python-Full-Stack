#WAP to check a number is Armstrong or not from given list
l = [1,2,5,6,9,23,34,56,153]
for i in l:
    lenth = len(str(i))     #3
    # print(lenth)
    num2 = str(i)   #153
    sum = 0
    for j in num2:
        sum = sum + int(j)**lenth
        if sum == i:
            print(i)
            break 
    else:
        continue
