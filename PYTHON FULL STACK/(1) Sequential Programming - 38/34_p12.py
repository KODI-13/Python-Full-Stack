#wap to check if number is prime or not from given list
l = [11,12,13,14,15,16,17]
for i in l:
    # print(range(i))
    for j in range(2,i):
        if i%j == 0:
            break 
    else: 
        print(i,"it is prime number")
