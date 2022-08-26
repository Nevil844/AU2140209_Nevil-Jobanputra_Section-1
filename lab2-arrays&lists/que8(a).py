class Node() :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self):
        self.head  = None
    
    def newnode(self, data):
        
        NewNode = Node(data)
        NewNode.next = self.head  
        self.head = NewNode
    def linstabeg(self, ele):
        nn = Node(ele)
        nn.next = self.head
        self.head = nn
        LinkedList.llprint(self)        
    
    def llprint(self):
        cur = self.head
        while cur != None:
            if cur.next == None:
                print(cur.data)
            else:
                print(cur.data, end=' --> ')
            cur = cur.next


l = LinkedList()
l.newnode(4)
l.newnode(3)
l.newnode(2)
l.newnode(1)

print("The Linked List : ")
l.llprint()  
print (l.linstabeg(55)) 


