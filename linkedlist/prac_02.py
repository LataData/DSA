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
    def isempty(self):
        if self.head==None:
            print("list is empty")
            return True
        else:
            return False
    def delete_from_front(self):
        if self.isempty():
            print("Please insert some value")
        else:
            temp=self.head.next
            self.head.next=None
            print("current head",self.head.data)
            self.head=temp
            print("current head",self.head.data)
            
    def delete_from_end(self):
        if (self.isempty() or self.head.next==None): #single node or no node
            self.head==None
            print("Please insert some value,list is empty now")
        else:
            temp=self.head
            prev=node(None)
            while( temp.next.next!=None):
                #print(temp.data)
                temp=temp.next
            temp.next=None
        
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
print("*="*12)
n1.delete_from_front()
n1.display()
print("*="*12)
n1.delete_from_end()
n1.display()



        
        
