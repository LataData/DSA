from prac_01 import stack as s
from prac_01 import Node
from reverse_stack import reverse
h=s()

def emptystack(m):
    while not m.isempty():
        print("hello")
        print(m.head.data())
        m.pop()
        
def reverse_word(text):
    for i in text:
        if text==" ":
            m=reverse(h)
            emptystack(m)
        else :
            #print(i)
            h.push(i)

reverse_word("hello hi")
