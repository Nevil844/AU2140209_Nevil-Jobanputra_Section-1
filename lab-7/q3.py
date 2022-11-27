# Q3. Implement Heapsort algorithm using Minheap.
# This must include building the heap as well as using it to sort an input array.
# The heapsort need not be done in-place.

class MinHeap():
    def __init__(self , Maximum_size):
        self.ele = []
        self.size = 0
        self._len = Maximum_size

    
    def lenHeap(self):
        return self.size

    
    def addNode(self, data):

        assert self.size < self._len, " Error! : The Heap is Full :-("

        self.ele.append(data)
        self.size = self.size + 1
        self.moveUp(self.size-1)

        return


    def moveUp(self,_index):
        if _index == 0:
            return
        if _index > 0 :
            p = (_index - 1) // 2 
               
        if (self.ele[_index] < self.ele[p]): 
            self.ele[_index], self.ele[p] = self.ele[p], self.ele[_index]
            self.moveUp(p)

        return


    def delNode(self):
        assert self.size>0, " Error! : The Heap is Empty :-("

        root_data = self.ele[0]
        self.size = self.size - 1
        self.ele[0] = self.ele[self.size]
        self.moveDown(0)

        return root_data
    
    def moveDown(self, _index):

        left_child = (2*_index) + 1
        right_child = (2*_index) + 2

        if(left_child < self.size and self.ele[_index] >= self.ele[left_child]):

            tmp = self.ele[left_child]
            self.ele[left_child] = self.ele[_index]
            self.ele[_index] = tmp
            self.moveDown(left_child)
        
        if(right_child < self.size and self.ele[_index] >= self.ele[right_child]):

            tmp = self.ele[right_child]
            self.ele[right_child] = self.ele[_index]
            self.ele[_index] = tmp
            self.moveDown(right_child)
        
        return



arr = [5,6,8,4,9,3,1,7,11,204]
n = len(arr)
print("\nUnsorted Array : ",arr)

sort_heap = MinHeap(n)
for i in range(n):
    sort_heap.addNode(arr[i])

for j in range(n):
    arr[j] = sort_heap.delNode()

print("Sorted Array : ",arr)
