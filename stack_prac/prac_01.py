class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            print("stack is empty....\n")
            return True
        else:
            return False
    def push(self,data1):
        newnode=Node(data1)
        #incase this is the very first node
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty()==True:

            return None
        else :
            temp=self.head
            self.head=temp.next
            temp.next=None
            print("Item deleted",temp.data)
            print("\n")
    def display(self):
        if self.isempty():
            print("stack is empty!!!")
        else:
            print("items present in stack")
            temp=self.head
            while(temp!=None):
                print(temp.data)
                temp=temp.next
new=stack()
new.head=Node(5)
new.push(7)
new.display()
print("*=*"*25)
new.pop()
new.display()
new.push(9)
new.push(11)
new.display()
new.pop()
new.pop()
new.pop()
new.display()

new.push(121)
new.display()
new.pop()
new.display()
