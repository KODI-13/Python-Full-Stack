import numpy as np
# python has list which works like array but list is heterogeneous collection of data and array contains similar type of data

l = [1,2,3,4]
print(type(l))

ar = np.array(l)
print(type(ar))
print(ar)

l = [2200,2350,2600,2130,2190]
# 1. In Feb, how many dollars you spent extra compare to January?
diff = l[1] - l[0]
print(diff)

# 2. Find out your total expense in first quarter (first three months) of the year.
total = l[0] + l[1] + l[2]
print(total)

# 3. Find out if you spent exactly 2000 dollars in any month
for i in l:
    index = 0
    if i == 2000:
        print('2000 at index', index)
    index += 1

print("Did I spent 2000$ in any month? ", 2000 in l) # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
l.append(1980)
print(l)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
april = l[3] - 200
l[3] = april 
print(l)


print('='*100)
heros=['spider man','thor','hulk','iron man','captain america']
# (Hint. Use dir() functions to list down all functions available in list)
print(heros.__dir__())

# 1. Length of the list
print(len(heros))

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.pop()
print(heros)
heros.insert(3,'black panther')
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.
# heros[1,2] = 'doctor strange'
# heros.replace()
# __setattr__(heros[1],'doctor strange')
heros[1:3] = ['doctor strange']
print(heros)

# 5. Sort the heros list in alphabetical order 
heros.sort()
print(heros)


# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
num = int(input(("Enter a numer : ")))
l=[]
for i in range(1,num):
    if i%2 != 0:
        l.append(i)
print(l)