# Q3. Implement Heapsort algorithm using Minheap.
# This must include building the heap as well as using it to sort an input array.
# The heapsort need not be done in-place.

class BinaryTree():
    def __init__(self , maxSize):
        self.ele = []
        self.size = 0
        self._len = maxSize

    
    def insert(self, data):

        assert self.size < self._len, " Error! : The Binary Tree is Full :-("

        self.ele.append(data)
        self.size = self.size + 1

        return


    def remove(self):
        assert self.size>0, " Error! : The Binary Tree is Empty :-("

        root_data = self.ele[0]
        self.size = self.size - 1
        self.ele[0] = self.ele[self.size]

        return root_data

    def minimum(self):
        fing = Queue()
        fing.enqueue(0)
        min_e = 0
        while not fing.isEmpty():
            ch = fing.dequeue()
            if(self.ele[ch]< self.ele[min_e]):
                min_e = ch
            else:
                chLeft = (ch*2)+1
                chRight = (ch*2)+2
                if chLeft < self.size:
                    fing.enqueue(chLeft)
                if chRight < self.size:
                    fing.enqueue(chRight)

        return self.ele[min_e]
    
    def printbinarytree(self):
        cnt = 0
        j = 1  
        print(" : The Binary Tree : ") 
        for i in range(self.size):  
            print(self.ele[i], end=" ")
            if (i == j-1):
                cnt += 1
                j = j + 2**cnt
                print("")
        print("")



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


arr = [5,6,8,4,9,3,1,7,11,204]
n = len(arr)
Binary_Tree = BinaryTree(n)
print("\n Inserting the array into the Tree : ", arr,"\n")
for i in range(n):
    Binary_Tree.insert(arr[i])

Binary_Tree.printbinarytree()

print("\n Removing from from the tree : ", Binary_Tree.remove())
print("After removing : The Tree ==> ")
Binary_Tree.printbinarytree()

print("\nThe Minimum Element in the Binary Tree : ", Binary_Tree.minimum(),"\n")