class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, node):

        if self.length == 0:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            
            current.next = node
        
        self.length +=1


    def printlist(self):

        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    
    def prepend(self, node):

        if self.length == 0:
            self.head = node
        else:
           # node.next = self.head  # Point new node to the current head
           # self.head = node  
           current = self.head 
           self.head = node
           self.head.next = current
                            
    def delete(self, data):

        current = self.head
        precurrent = None
        target = None
        while current != None:
            if current.data == data:
                target = current.data
                break
            else:
                precurrent = current
                current = current.next

        precurrent.next = current.next           
        current = None
        self.length -= 1
        return target
    
    def search(self,data):

        current = self.head

        while current != None:
            if current.data == data:
                return current.data
            else:
                current = current.next

    def Length(self):

        len = 0
        current = self.head

        while current != None:
            len += 1
            current = current.next

        return len

    def insert(self, node, pos):
        
        if pos < 0 or pos > self.length:
            return None
        
        elif pos == 0:

            node.next = self.head  # Point new node to the current head
            self.head = node  

        elif pos == self.length :

            if self.length == 0:
                self.head = node
            else:
                current = self.head
                while current.next != None:
                    current = current.next
            
                current.next = node

        else:

            precurrent = None
            current = self.head
            position = 0
            
            while current != None:

                if position == pos:
                    break 
                else:
                    precurrent = current
                    current = current.next 
                position +=1 

            precurrent.next = node
            node.next = current
            current = None

        self.length +=1

linkedlist1 = LinkedList()
linkedlist1.append(Node(10))
linkedlist1.append(Node(20))
linkedlist1.append(Node(30))
linkedlist1.prepend(Node(5))
linkedlist1.insert(Node(8), 2)
linkedlist1.printlist()
print(f"The length of the list is: {linkedlist1.Length()}")
print("===========================================")
print(f"You removed {linkedlist1.delete(20)}")
print("===========================================")
linkedlist1.printlist()
print(f"The length of the list is: {linkedlist1.Length()}")
print("===========================================")
print("We are searching for the node holding the value 10 if we found it we will return its data: ")
print(linkedlist1.search(10))