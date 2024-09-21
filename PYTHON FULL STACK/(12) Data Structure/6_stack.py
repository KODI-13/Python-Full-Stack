"""
list is a stack implementation in python 
stack is lifo data structure that is last in first out means the last elemnt u push in the stack is poped first
it has two operation push and pop in short it is called as lifo operation
"""
s = []
s.append("https://edition.cnn.com/")
s.append("https://edition.cnn.com/us")
s.append("https://edition.cnn.com/world")
s.append("https://edition.cnn.com/world/asia")
print(s)
s.pop()
print(s)

"""
stack implementatioon using list in the insertion opertation complexity will be o(n) thats why it is not recommended
so we use collection.deque so it is a double linked list so we dont have to worry about the copying current element into the new memeory location
it will alocate memory as we nedded
"""
from collections import deque
stack = deque()
print(dir(stack))

stack.append("https://edition.cnn.com/")
stack.append("https://edition.cnn.com/us")
stack.append("https://edition.cnn.com/world")
stack.append("https://edition.cnn.com/world/asia")
print(stack)

stack.pop()
print(stack)


