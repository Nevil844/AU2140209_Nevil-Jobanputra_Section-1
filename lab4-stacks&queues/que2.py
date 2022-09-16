class Stack :

    # Creates an empty stack.
    def __init__( self ): 
        self._top = None 
        self._size = 0
    
    # Returns True if the stack is empty or False otherwise.
    def isEmpty( self ): 
        return self._top is None
    
    # Returns the number of items in the stack.
    def __len__( self ): 
        return self._size

    # Returns the top item on the stack without removing it.
    def peek( self ):
        assert not self.isEmpty(), "Cannot peek at an empty stack" 
        return self._top.item
    
    # Removes and returns the top item on the stack.
    def pop( self ):
        assert not self.isEmpty(), "Cannot pop from an empty stack" 
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item
    
    # Pushes an item onto the top of the stack.
    def push( self, item ) :
        self._top = _StackNode( item, self._top ) 
        self._size += 1
    def postfixexpression(self,input):
      for i in input:
        if (i=="+" or i=="*" or i=="-" or i=="/"):
            i=str(i)
            val1 = str(self.pop())
            val2 = str(self.pop())
            self.push(str(eval(val2 + i + val1)))
        else:
          self.push(i)
      return self.pop()
    def printstack(self):
      if self.isEmpty()==True:
        print('None')
      else:
        temp=self._top
        while temp!=None:
          print(temp.item,end=" ")
          temp=temp.next
# The private storage class for creating stack nodes.
class _StackNode :
    def __init__( self, item, link ) :
        self.item = item
        self.next = link
print("Enter the expression")
input1= list(input().split())
print(input1)
myS = Stack()
print("Output of the postfix expression : ",myS.postfixexpression(input1))