def get_hash(key):  #it takes string as key
    h = 0
    for char in key:
        h += ord(char)          # ord function find ascii valuenof a character
    return h % 100          # it gives mod i.e mod(h,100) means h is divided by 100 (which is size of array) and the remainder as an output will be returned which is the position of or index number where the value is stored

print(ord('m'))     # ord function find ascii valuenof a character

print(get_hash('march 6'))


# we are implementing dictionary to see how hash table data structure works
class HashTable:
    def __init__(self) -> None:
        self.Max = 100
        self.arr = [None for i in range(self.Max)]          # created a list/array using list comprehension and the value for each is sset to be None

    def get_hash(self,key):  #it takes string as key
        h = 0
        for char in key:
            h += ord(char)          # ord function find ascii valuenof a character
        return h % self.Max    
    
    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    # above two functionns can be implemented like below two function (below three function works like operation in dictionary)
    # to do operation like dictionary we are going to override predeined item operator
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
print(t.get_hash('march 6'))
print(t.add("march 6", 310))
print(t.arr)
print(t.get("march 6"))

print("="*100)
t['march 9'] = 123
t['march 1'] = 40
t['dec 19']  = 23
print(t.arr)
print(t['march 9'])
print(t['march 1'])
print(t['dec 7'])
print(t['dec 19'])

print("="*100)
del t['march 1']
print(t['march 1'])
print(t.arr)