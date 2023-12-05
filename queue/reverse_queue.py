#reverse queue using stack
from collections import deque
class Reversal:
    def __init__(self):
        self.q=deque()
    def insert(self,ele):
        self.q.append(ele)
    def remove(self):
        if len(self.q)==0:
            return None
        else:
            return self.q.popleft()
    def reverse(self):
        if len(self.q)==0:
            return None
        else:
            s=deque()
            print("Before reversal",self.q)
            while len(self.q)!=0:
                s.appendleft(self.remove())
            while len(s)!=0:
                self.insert(s.popleft())
            print("after reversal",self.q)
            
r=Reversal()
r.insert(5)
r.insert(7)
r.insert(8)
r.reverse()
