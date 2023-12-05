class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Q:
    def __init__(self):
        self.rear=None
        self.front=None                       
    def enqueue(self,value):
        newnode=Node(value)
        if self.front==None:
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            newnode=self.rear
    def dequeue(self):
        if self.front==None:
            return -1
        else:
            temp=Node(None)
            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp.data
h=Q()
h.enqueue(5)
h.enqueue(10)
print(h.dequeue())
print(h.dequeue())
print(h.dequeue())

