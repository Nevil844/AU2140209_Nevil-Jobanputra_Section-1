class Node() :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LL :
    def __init__(self):
        self.head  = None
    
    def newnode(self, data):
        
        NewNode = Node(data)
        
        NewNode.next = self.head  

        self.head = NewNode
    
    def lsrch(self, e): 
        nc = self.head
        i = 1
        while nc != None: 
            if nc.data == e :
                return i
            nc = nc.next
            i = i + 1

        return -1
    
    def llprint(self):
        nc = self.head
        while nc != None:
            if nc.next == None:
                print(nc.data)
            else:
                print(nc.data, end=' --> ')
            nc = nc.next

# Starting :

l = LL()
l.newnode(10)
l.newnode(11)
l.newnode(12)
l.newnode(13)

print("The Linked List : ")
l.llprint()  

print ("The index number of element '10' is : ",l.lsrch(10)) 


