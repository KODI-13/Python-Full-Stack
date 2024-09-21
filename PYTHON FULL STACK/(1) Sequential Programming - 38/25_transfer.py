"""
flow control statement --> use to control the flow of statement
1) conditional statement
        a) if statement
        b) if else statement
        c) if elif else statement
2) iterative statement
        a) for loop 
        b) while loop
        c) while True
3) transfer statement
        a) pass -- hold the block/body for future use
        b) continue --> skip current iteration
        c) break --> Terminates the loop
""" 

l = [11,22,33,44,55,66]
for i in l:
    if i%2 == 0:
        pass

k = [11,22,33,44,55,66]
for j in k:
    if j == 33:
        continue  
    print(j)

m = [11,22,33,44,55,66]
for u in m:
    if u%2 == 0:
        continue  
    print(u)


#2nd method when we don't know what is odd number
z = [11,22,33,44,55,66]
for p in z:
    if p%2 != 0:
        continue 
    print(p) 
