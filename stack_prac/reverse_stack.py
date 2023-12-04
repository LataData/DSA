from prac_01 import stack as s
from prac_01 import Node
h=s()
m=s()
#h.head=Node(7)

def reverse(h):
    if not h.isempty():
        m.push(h.pop())
        
        return reverse(h)
    else:
        return m

'''h.push(7)
h.push(8)
h.push(9)
reverse(h)


while not m.isempty():
    print(m.head.data)
    m.pop()'''