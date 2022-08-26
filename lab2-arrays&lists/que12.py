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

def doubbly_remove(ll,elem):

    newHead = ll.head
    newTail = ll.tail
    curr = ll.head
    flg = True

    while(curr):
        if(curr.data == elem):

            if(curr.next == None and curr.prev != None):
                newTail = curr.prev
                curr.prev.next = None
                curr.prev = None
                break

            elif(curr.prev == None and curr.next != None):
                newHead = curr.next
                curr.next.prev = None
                curr.next = None
                break

            else:
                curr.next.prev = curr.prev
                curr.prev.next = curr.next
                curr.prev = None
                curr.next = None
                break

        curr = curr.next
    else:
        print("ELement Not in Doubly Linked List !")
        flg = False

    ll.head = newHead
    ll.tail = newTail

    if(flg):
        ll.showLink()

a = Node(11)
b = Node(22)
c = Node(33)
a.next = b

b.prev = a
b.next = c

c.prev = b

ll = LinkedList(a,c)
remove = 22
print("Original Doubly Linked List:")
ll.showLink()
print("Doubly Linked List After Deletion of",remove,":")

doubbly_remove(ll,remove)
