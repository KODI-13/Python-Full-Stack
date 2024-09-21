"""
range() ---> it is function as well as collective data type                             
syntax: var_name = range(whole_number) ....where whole number is end number and start value is by default 0
syntax: var_name = range(start_value,end_value - 1) 
syntax: var_name = range(start_value,end_value - 1, step_value) 
"""

r = range(5) 
print(r)

p = range(10)
for i in p:
    print(i) 

q = range(1,12)
for j in q:
    print(j) 

#shortcut method 

for i in range (10,21):
    print(i)

for j in range (25,46):
    print(j) 

for k in range (2,11,2):
    print(k) 

for l in range (10,0,-1):
    print(l) 

print("="*100)
# printing backword without step minus value then it does not give error but also don't show output
for s in range (21,10):
    print(s)

for s in range (21,10,-1):
    print(s)
