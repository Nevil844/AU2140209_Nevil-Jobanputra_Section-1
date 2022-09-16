# Private storage class for associating queue items with their priority.
class _PriorityQEntryl:

    def __init__( self, item, priority ):
        self.item = item
        self.priority = priority
        self.next = None
      
class PriorityQueueL:
  

    # Create an empty unbounded priority queue.
    def __init__( self ):
        self._qhead = None
        self._qtail = None
        self._size = 0


    # Returns True if the queue is empty.
    def isEmpty( self ):
        return self._qhead is None

    # Returns the number of items in the queue.
    def _len_( self ):
        return self._size

    # Adds the given item to the queue.
    def enqueue( self, item, priority ):
        
        # Create a new instance of the storage class and append it to the list.
        node = _PriorityQEntryl( item, priority )
        
        if self.isEmpty() :
            self._qhead = node
        else :
            self._qtail.next = node
        
        self._qtail = node
        self._size += 1
        

    # Removes and returns the first item in the queue.
    def dequeue( self ) :
        
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."

        # Find the entry with the highest priority.
        node = self._qhead
        
        highpri  = self._qhead.priority 
        highnode = self._qhead
        
        #print("higher..", highnode.item, highnode.priority)
        
        while node !=  None :
            # See if the next entry contains a higher priority (smaller integer).
            if node.priority < highpri : 
                highpri  = node.priority
                highnode = node
                prevhigh = prevnode # the node prev to highnode
                #print("higher..", highnode.next.item, highnode.next.priority)            

            prevnode = node
            node = node.next


        # Remove the entry with the highest priority and return the item.
        node = highnode

        if self._size == 1: 
            self._qtail = None
            self._qhead = None
            self._size = 0
        else:
            if node is self._qhead:
                self._qhead = self._qhead.next 
            else:
                prevhigh.next = node.next

            self._size -= 1

        return node.item
  
    # Print PQ
    def prnpq ( self ):
        node = self._qhead
        while node != None:
            print(node.item,node.priority)
            node = node.next