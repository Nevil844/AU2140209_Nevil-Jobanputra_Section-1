class node:
    def _init_(self,data):
        self.data=data
        self.next=None

class queue:
    def _init_(self):
        self.head=self.tail=None
        self.qsize=0

    def isempty(self):
        return self.head==None

    def queuelen(self):
        return self.qsize

    def enqueue (self,item):
        a=node(item)
        if self.isempty():
            self.head=a 
        else :
            self.tail.next=a
        self.tail=a
        self.qsize+=1

    def dequeue(self): 
        assert self.head!=None
        if (self.head==self.tail):
            self.head=self.tail=None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.qsize-=1
        return temp.data