"""
operators --> Operators are used to perform operations on variables and values or oprands
              an operator is a symbol that performs an operation or manipulation on one or more operands. 

1)arithmatic --> to perform common mathematical operations
        +  addition (it concate the string,list and tuple and gives error for set and dictionary )
        -  substraction
        *  multiplication (in case of string it print string multiplyed by that number in concate format)
        /  divison (it gives output in float format)
        // flow division (it gives output in inteager format...it discard the value ahead point)
        ** power operator 
        %  modulous (it gives the remainder) 

2)Relational (it compares the both sides and alwyas return output (value) in boolean format) 
        >  greater than
        >= greater than and equal to
        <  less than
        <= less than and equal to
        == equal to equal
        != not equal to 
        =  assign operator 

3)logical (connects two or more than two conditions and always return output (value) in boolean format)
        and --> we use it when both condtions are mandeatory..... if both are true then it gives true
        or  --> we use it when two out of one condtions are mandeatory.....if one of two is ready then it gives true
        not --> it reverse the condition

4) Assignment Operators: Assign values to variables.
                         Examples: =, += (add and assign),
                                      -= (subtract and assign),
                                      *= (multiply and assign), 
                                      /= (divide and assign).

5) Bitwise Operators: Perform bit-level operations on integers.
                      Examples: & (bitwise AND),
                                | (bitwise OR), 
                                ^ (bitwise XOR),
                                ~ (bitwise NOT), 
                                << (left shift), 
                                >> (right shift).
6) special operator:
  in (this operator called as 'membership operator' and always return output (value) in boolean format)
        check membership of particular element.....and use in conditions i.g. if else

  is (it checks the whether the memory location of two variable is same or not and always return output (value) in boolean format....this operator called as 'identity operator')

natural numbers == 1,2,3,4,5
odd numbers == 1,3,5,7,9    (the number is not completely divisible by 2 )
even numbers == 2,4,6,8,10  (the number completely divisible by 2 is called as even numbers)
prime numbers == 2,3,5,7,11

""" 

# d1 = {1,2,3}
# d2 = {2,3,4}
# print(d1+d2)

# d1= {"name":"deep"}
# d2 = {"name":"sidhhi"}
# print(d1+d2)

l = [1,2,3]
print(l*2)

t = (11,22,33)
print(t*2) 

n1 = 20
n2 = 5
print(n1/n2)

m1 = 30 
m2 = 7
print(m1//m2) 

k1 = 100                       #Two variables with different name and same value are assign on same memory locatioin 
k2 = 100
print(k1 is k2) 
print(id(k1))
print(id(k2))

k1 = 100,200                   #Two variables with different name and same value are assign on same memory locatioin 
k2 = 100,200
print(k1 is k2) 
print(id(k1))
print(id(k2))

l1 = [11,22,33]                #ONLY list data don't assign two variables same memeory location whether they both have same value stored in it
l2 = [11,22,33]
print(l1 is l2)

l3 = [11,22,33,11]             #but the memory location of duplicate content in list data is same
l4 = [11,22,33]
print(id(l3))
print(id(l3[0]))
print(id(l3[3]))
