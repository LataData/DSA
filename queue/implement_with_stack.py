#from prac_01 import stack as s
#import sys
#sys.path.insert(0,'F:DSA\stack_prac')
#implement stack first
from collections import deque
class que:
    def __init__(self):
        self.s1=deque()
        self.s2=deque()
    def insert(self,ele):
        while  len(self.s1)!=0:
            self.s2.appendleft(self.s1.popleft())
        print("s2  ",self.s2)
        self.s1.appendleft(ele)
        while  len(self.s2)!=0:
            self.s1.appendleft(self.s2.popleft())
        print(self.s1,"      bjkhkjkk")
    def remove(self):
        if len(self.s1)==0:
            return None
        else:
            return self.s1.popleft()
k=que()
k.insert(8)
k.insert(9)
print(" deleted",k.remove())
k.insert(90)
k.insert(20)
print(" deleted",k.remove())
print(" deleted",k.remove())