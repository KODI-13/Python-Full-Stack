"""
staack has follwoing methods
"""

from collections import deque
class Stack:
    def __init__(self) :
        self.container = deque()

    def push(self,val):
        self.container.append(val)
    
    def pop(self):                      # it delete last element u enter also return it
        return self.container.pop()

    def peek(self):                     # it return first element u enter but does not delete it
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    # def reverse_string(self,val):
    #     self.container.append(val)
    #     reverse = ''
    #     for i in val:
    #         reverse += s.pop()
    #     return reverse
    
s = Stack()
print(s.is_empty())
print(s.size())
s.push(5)
print(s.peek())
s.push(10)
print(s.container)
print(s.peek())
s.push(15)
s.push(20)
s.push(25)
print(s.size())
# print(dir(s.container))


# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr
print(reverse_string("i am"))

# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True