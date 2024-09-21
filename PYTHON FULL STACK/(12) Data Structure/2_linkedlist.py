"""
linked list --> linked list is data struture containing node where each node has data and refernce to next node
                Common types include singly linked lists and doubly linked lists.
"""

class node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next  # python keyword .. c and java has conept like null

class LinkedList:
    def __init__(self):
        self.start = None 

    #Inserting a node at end
    def insert_at_end(self, value):
        newNode = node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None: 
                temp = temp.next
            temp.next = newNode
    
    #Inserting a node at begining
    def insert_at_begining(self, value):
        newNode = node(value,self.start)
        self.start=newNode

    #Inserting a node at particular input index
    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        temp = self.start
        while temp:
            if count == index -1:
                nd = node(data, temp.next)
                temp.next = nd
                break
            temp = temp.next
            count += 1


    #Inserting a Data_list 
    def inserting_values(self,data_list):
        self.start = None
        for data in data_list:
            self.insert_at_end(data)

    # Deleting first node
    def deleteFirst(self):
        if self.start == None:
            print("Linked list is empty")
        
        else:
            # temp = self.start
            self.start = self.start.next

    # counting the lenth of linked list
    def get_length(self):
        counter = 0
        temp = self.start
        while temp:
            counter += 1
            temp = temp.next
        return counter

        
    # deleting a particular node with given input index
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        
        if index == 0:
            self.start = self.start.next
            return
        
        count = 0
        temp = self.start
        while temp:
            if count == index -1:
                temp.next = temp.next.next
                break
            temp = temp.next
            count += 1

    # to travers the linked list
    def viewList(self):
        if self.start == None:
            print("Linked list is empty")
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end="-->")
                temp = temp.next

            # llstr = ''
            # while temp:
            #     llstr += str(temp.data) + '-->'
            #     temp = temp.next
            # print(llstr)

    #insert data after given value  
    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        if self.start == None:
            print("Linked list is empty")

        if self.start.next == data_after:
            self.start.next = node(data_to_insert,self.start.next)

        temp = self.start
        while temp:
            if data_after == temp.data:
                nd = node(data_to_insert,temp.next)
                temp.next = nd
                break
            temp = temp.next

    def remove_by_value(self, data):
    # Remove first node that contains data
        if self.start == None:
            print("Linked list is empty")

        if self.start.data == data:
            self.start = self.start.next
            return
        
        temp = self.start
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                break
            temp = temp.next

mylist = LinkedList()
mylist.insert_at_end(10)
mylist.insert_at_end(20)
mylist.insert_at_end(30)
mylist.insert_at_end(40)
mylist.viewList()
print()
mylist.deleteFirst()
mylist.viewList()
print()
mylist.insert_at_begining(9)
mylist.viewList()
print()
mylist.get_length()
print()
mylist.remove_at(0)
mylist.viewList()
print()


mlist = LinkedList()
mlist.inserting_values(['banana','apple','mango','orange','pineapple'])
mlist.viewList()
print()
mlist.get_length()
print()
mlist.remove_at(3)
mlist.viewList()
print()
mlist.insert_at(0,'dragonfruit')
mlist.insert_at(2,'jackfruit')
mlist.viewList()
print()
mlist.insert_after_value('apple','grapes')
mlist.viewList()
print()
mlist.remove_by_value('apple')
mlist.viewList()
print()

ll = LinkedList()
ll.inserting_values(["banana","mango","grapes","orange"])
ll.viewList()
print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.viewList()
print()
ll.remove_by_value("orange") # remove orange from linked list
ll.viewList()
print()
ll.remove_by_value("figs")
ll.viewList()
print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.viewList()
print()


