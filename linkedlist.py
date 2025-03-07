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
            node.next = self.head  # Point new node to the current head
            self.head = node  
                            
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
        return target

linkedlist1 = LinkedList()
linkedlist1.append(Node(10))
linkedlist1.append(Node(20))
linkedlist1.append(Node(30))
linkedlist1.prepend(Node(5))
print(f"You removed {linkedlist1.delete(20)}")
linkedlist1.printlist()