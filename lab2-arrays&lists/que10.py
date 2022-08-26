class Node:
 
   
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:

    def __init__(self,head):
        self.head = head
    
    def showLink(self):
        curr = self.head
        l = list()
        while(curr):
            l.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(l))

def replatind(ll,pos,ele):
    cont = 1
    curr = ll.head
    flg = True

    while(curr):
        if(cont==pos):
            curr.data =ele
            break
        cont+=1
        curr =curr.next
    else:
        print(-1)
        flg =False
    
    if(flg):
        ll.showLink()

a=Node(1)
b=Node(2)
c=Node(3)

a.next=b
b.next=c

ll = LinkedList(a)
ind = 2
rep = 7

print("Original Linked List: ")
ll.showLink()
print("Linked List After Replacing Element at Index",ind,"with",rep,":")

replatind(ll,ind,rep)