from prac_01 import linkedlist as l
from prac_01 import node

def reverse_list(self):
        if self.head==None or self.head.next==None:
            return True
        else:   
            temp=self.head
            prev=None
            while(temp!=None):
                
                nextnode=temp.next
                temp.next=prev
                prev=temp
                temp=nextnode
                

            self.head=prev
n1=l()
n1.head=node(1)
n1.insert_in_front(6)
n1.insert_in_front(9)
n1.insert_in_front(12)
n1.insert_in_end(18)
n1.display()
reverse_list(n1)
n1.display()