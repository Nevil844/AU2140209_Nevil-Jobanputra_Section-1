class Node() :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.tail = None

class LinkedList :
    def __init__(self):
        self.head  = None
        self.tail = None

    def newnode(self, data):
        
        NewNode = Node(data)
        NewNode.next = self.head
        if self.tail == None and self.head == None:
            self.tail = NewNode

        self.head = NewNode

    def delatend(self):
        nc = self.head
        while nc != None:
            if nc.next.next == None:
                nc.next = None
                break
            nc = nc.next
        LinkedList.llprint(self)

    def llprint(self):
        nc = self.head
        while nc != None:
            if nc.next == None:
                print(nc.data)
            else:
                print(nc.data, end=' --> ')
            nc = nc.next


l = LinkedList()
l.newnode(4)
l.newnode(3)
l.newnode(2)
l.newnode(1)

print("The Linked List : ")
l.llprint() 

print (l.delatend()) 


