class Node:
 
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:

    def __init__(self,head,tail):
        self.head = head
        self.tail = tail
    
    def showLink(self):
        curr = self.head
        l = list()
        while(curr):
            l.append(str(curr.data))
            curr = curr.next
        print(" <=> ".join(l))

def dubbly_append(ll,elem):
    curr = ll.head
    z = Node(elem)

    while(curr):
        if(curr.next == None):
            curr.next = z
            z.prev = curr
            break
        curr = curr.next

    ll.showLink()


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b

b.prev = a
b.next = c

c.prev = b

ll = LinkedList(a,c)
add = 4

print("Original Doubly Linked List:")
ll.showLink()
print("Doubly Linked List After Appending",add,":")

dubbly_append(ll,add)