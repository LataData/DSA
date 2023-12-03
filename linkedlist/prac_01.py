class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_in_front(self,value):
        newnode=node(value)
        if self.head!=None:
            newnode.next=self.head
        self.head=newnode
    def insert_in_end(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while( temp.next !=None):
                #print(temp.data)
                temp=temp.next
            temp.next=newnode
        
    def display(self):
        if self.head==None:
            print("list is empty")
        else:
            temp=self.head
            while( temp!=None):
                print(temp.data)
                temp=temp.next
            

      
        
n1=linkedlist()
n1.head=node(1)
n1.insert_in_front(6)
n1.insert_in_front(9)
n1.insert_in_front(12)
n1.insert_in_end(18)
n1.display()



        
        
