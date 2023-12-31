from prac_01 import stack as s
from prac_01 import Node
class postfix:
    def __init__(self):
        self.top=-1
        self.precedence={'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.output=[]
    def test(self):#,expression):
        #n1=Node(None)
        h=s()
        #h.head=None)
        h.push(5)
        self.top=h.peek()
        print("display...")
        h.display()
        print("top...",self.top)
    def notGreater(self,i,head):
        try: 
            if self.precedence[i]<=self.precedence[head.peek()]:
                return True
            else:
                return False
        except KeyError:
            return False
            

    def conversion(self,expression):
        head=s()
        for i in expression:
            if i.isalpha():
                self.output.append(i)
            elif i=='(':
                head.push(i)
            elif i==')':
                while (not head.isempty()) and (head.peek!='('):
                    a=head.pop()
                    self.output.append(a)
                if (not head.isempty() and head.peek() != '('):
                    return -1
                else:
                    head.pop()
            else:
                while(not head.isempty() and \
                      self.notGreater(i,head)):
                    self.output.append(head.pop())
                head.push(i)
        while not head.isempty():
            self.output.append(head.pop())
        for ch in self.output:
            print(ch, end="")



p=postfix()
#p.test()
exp = "a+b*c"
exp2="a+b*(c^d-e)^(f+g*h)-i"

p.conversion(exp2)
