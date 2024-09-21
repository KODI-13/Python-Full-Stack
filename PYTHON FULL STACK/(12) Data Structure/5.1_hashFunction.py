# we are implementing dictionary to see how hash table data structure works
"""
for handling collision of keys -->
collsionmeans if e are getting same index on different keys to dtore value in the array then we use two approch or methods
1) separate chaining ( storing both value at the same index in the form of array or linked list in that case the bi9g o complexity becomes O(n)  )
2) linear probing (if both keys shopwing same index then we linarly probing(i.e. searching) for next available position ini the array)
"""
class HashTable:
    def __init__(self) -> None:
        self.Max = 100
        self.arr = [[] for i in range(self.Max)]          # created a list/array using list comprehension and the value for each is sset to be None

    def get_hash(self,key):  #it takes string as key
        h = 0
        for char in key:
            h += ord(char)          # ord function find ascii valuenof a character
        return h % self.Max    
    
    # def add(self,key,value):
    #     h = self.get_hash(key)
    #     self.arr[h] = value

    # def get(self,key):
    #     h = self.get_hash(key)
    #     return self.arr[h]
    
    # above two functionns can be implemented like below two function (below three function works like operation in dictionary)
    # to do operation like dictionary we are going to override predeined item operator
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,value)                  # element[1] = value
                found = True
                break
        
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

t = HashTable()
print(t.get_hash('Apr 04'))
print(t.get_hash('Mua 04'))      #overriding the value of first key because both are storing at same location
t['Apr 04'] = 123
t['Mua 04'] = 459

print(t['Apr 04'])
print(t['Mua 04'])

print(t.arr)

del t['Mua 04']
print(t['Mua 04'])
print(t.arr)
