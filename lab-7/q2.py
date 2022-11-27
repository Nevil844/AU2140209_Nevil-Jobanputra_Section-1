# Q2. Implement breadth first search on a tree (not necessarily binary).
# The input is given in a file with the following format:

# node node-nbr1 node-nbr2 node-nbr3 ...

# e.g.:
# 5 1 2 3
# 1 3
# 2 6 7
# 3 7 8 9

class QueueNode :
    def __init__(self, data) :
        self.data = data
        self.next = None

class Queue :
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return (self.head == None)

    def length_(self):
        return self.size 

    def enqueue(self, data):
        
        newQueueNode = QueueNode(data)
        
        if self.head == None:
            self.head = newQueueNode
            self.tail = newQueueNode
            self.size +=1
        else:
            self.tail.next = newQueueNode
            self.tail = newQueueNode
            self.size +=1
        
    def dequeue(self):
        assert self.tail != None, " Cannot dequeue from empty Queue :-( "
        data = self.head.data
        self.head = self.head.next
        self.size -=1
        return data



class TreeNode():
    def __init__(self,data):
        
        self.data = data
        self.left = None
        self.right = None

    def Leftinsert(self, leftnode):
        self.left = leftnode
    
    def Rightinsert(self, rightnode):
        self.right = rightnode
    
    def printTree(self):
        print(self.data, end=" ")
        if (self.left):
            self.left.printTree()
        if(self.right):
            self.right.printTree()

def BreadthFirstSearch(root,ele):
    if root is None:
        return
    else:
        c = -1
        bfs = Queue()
        bfs.enqueue(root)
        while not bfs.isEmpty():
            ch = bfs.dequeue()
            if(ch.data == ele):
                c = 0
                return True
            else:
                if ch.left != None:
                    bfs.enqueue(ch.left)
                if ch.right != None:
                    bfs.enqueue(ch.right)
        if (c== -1):
            return False



g = TreeNode(1)
g1 = TreeNode(5)
g2 = TreeNode(6)
g3 = TreeNode(7)
g4 = TreeNode(8)
g5 = TreeNode(9)
g.Leftinsert(g1)
g.Rightinsert(g2)
g1.Leftinsert(g3)
g3.Rightinsert(g4)
g4.Leftinsert(g5)
print("Tree : ")
g.printTree()
print("\n")
print("Searching for 8 : ",BreadthFirstSearch(g,8))
print("Searching for 9 : ",BreadthFirstSearch(g,9))
print("Searching for 10 : ",BreadthFirstSearch(g,10))