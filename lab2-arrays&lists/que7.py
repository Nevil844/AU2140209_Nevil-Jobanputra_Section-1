class Node:
 
    def __init__(self, data):
        self.data = data  
        self.next = None  
class SLinkedList:

    def __init__(self,head):
        self.head = head
    
    def showLink(self):
        curr = self.head
        l = list()
        while(curr):
            l.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(l))

def linsatend(ll,elem):
    tmp=ll.head
    z=Node(elem)
    while(tmp):
        if(tmp.next==None):
            tmp.next=z
            break
        tmp=tmp.next

    ll.showLink()


a=Node(1)
b=Node(2)
c=Node(3)

a.next=b
b.next=c

ll = SLinkedList(a)
add = 55

print("Original Linked List:")
ll.showLink()
print("Linked List After Insertion of",add,"at End:")

linsatend(ll,55)