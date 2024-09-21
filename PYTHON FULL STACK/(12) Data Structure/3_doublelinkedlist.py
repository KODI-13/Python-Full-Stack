# from typing import Self


class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def Print(self):
        # if self.head == None:
        #     print("The Double linked list is empty ")
        # else:
            itr = self.head
            while itr:                  #itr.next != None
                suffix = " "
                if itr.next:
                    suffix = "<-->"
                print(itr.data,suffix,end=" ")
                itr = itr.next

    def print_forward(self):
        # This method prints list in forward direction. Use node.next    
            itr = self.head
            while itr:                  #itr.next != None
                suffix = " "
                if itr.next:
                    suffix = "<-->"
                print(itr.data,suffix,end=" ")
                itr = itr.next
    
    # def print_backward (self):
    #     # Print linked list in reverse direction. Use node.prev for this.
    #         itr = self.head
    #         while itr.next != None:                  #itr.next != None
    #             itr = itr.next
    #             suffix = " "
    #             if itr.next == None:
    #                 itr = itr.prev
    #                 print(1)
    #                 while itr.prev != None:
    #                         print(1)
    #                         suffix = "<-->"
    #                         print(itr.data, suffix,end=" ")
    #                         itr = itr.prev
    #                 break

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
            # last_node = self.get_last_node() 
            itr = self.get_last_node() 
            suffix = " "
            print("xyz")
            last_node = self.get_last_node()
            itr = last_node
            llstr = ''
            while itr:
                llstr += itr.data + '-->'
                itr = itr.prev
            print("Link list in reverse: ", llstr)


    def get_last_node(self):
        itr = self.head 
        while itr:
            itr = itr.next

        return itr



    def insert_at_begining(self,data):
        # self.head.prev = Node(data,self.head,None)            #AttributeError: 'NoneType' object has no attribute 'prev'
        if self.head == None:
            self.head = Node(data,self.head,None)
        else:
            nd =  Node(data,self.head,None) 
            self.head.prev = nd
            self.head = nd

    def insert_at_end(self,data):
        if self.head == None:
            self.insert_at_begining(data,None,None)
        else:
            itr = self.head
            while itr.next != None:
                itr = itr.next
            itr.next = Node(data,itr.next,itr)

    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            
        else:
            itr = self.head
            count = 0 
            while itr:
                if count == index - 1:
                    nd = Node(data,itr.next,itr)
                    if nd.next:
                        nd.next.prev = nd
                    itr.next = nd
                itr = itr.next
                count += 1

    # def deleteFirst(self):
    #     if self.head == None:
    #         print("The Double linlked list is empty")

    #     else:
    #         itr = self.head 
    #         # while itr:
    #         self.head = itr.next
    #             # itr = itr.next
    
    # def deleteLast(self):
    #     if self.head == None:
    #         print("The Double linked list is empty")

    #     else:
    #         itr = self.head 
    #         count = 1
    #         while itr.next != None:
    #             count += 1
    #             if count == self.get_length():
    #                 itr.next = None
    #                 break
    #             itr = itr.next

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.deleteFirst()

        else:
            itr = self.head
            count = 0
            while itr:
                if count == index :
                    itr.prev.next = itr.next
                    if itr.next:
                        itr.next.prev = itr.prev
                    break
                itr = itr.next
                count += 1


root = DoubleLinkedList()
root.insert_at_begining(13)
root.insert_at_begining(15)
root.insert_at_begining(20)
root.Print()
print()

root.insert_at_end(17)
root.Print()
print()

len = root.get_length()
print(len)

root.insert_at(1, 17)
root.Print()
print()

root.deleteFirst()
root.Print()
print()

root.deleteLast()
root.Print()
print()

root.remove_at(1)
root.Print()
print()

root.print_backward()
print()