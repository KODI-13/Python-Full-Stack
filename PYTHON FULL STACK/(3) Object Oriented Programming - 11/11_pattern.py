#rectangle star pattern
#l = length = 3
#w = width = 5
for i in range(3):
    for j in range(5):
        print("*",end = " ")
    print(end = "\n")

print()

for i in range(5):
    for j in range(10):
        print("*",end = " ")
    print(end = "\n")

print()

# Square Star pattern
for i in range(5):
    for j in range(5):
        print("*",end = " ")
    print(end = "\n")

print()

# Triangle Star pattern
for i in range(4):
    for j in range(i+1):
        print("*", end = " ")
    print(end = "\n")

print()

# Reverse Triangle Star pattern
num = 4
for i in range(num):
    for j in range(num-i):
        print("*", end = " ")
    print(end = "\n")

print()

num = 4
for i in range(num):
    for j in range(num-i):
        print(" ", end = " ")
    for k in range(i+1):
        print("*", end = " ")
    print(end = "\n")

print()

num = 4
for i in range(num):
    for j in range(num+i):
        print(" ", end = " ")
    for k in range(num-i):
        print("*", end = " ")
    print(end = "\n")

print()

# Center Triangle
num = 4
for i in range(num):
    for j in range(num-i):
        print("", end = " ")
    for k in range(i+1):
        print("*", end = " ")
    print(end = "\n")

print()

# reverse center traingle
num = 4
for i in range(num):
    for j in range(num+i):
        print("", end = " ")
    for k in range(num-i):
        print("*", end = " ")
    print(end = "\n")