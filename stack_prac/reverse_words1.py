from prac_01 import stack as s
from prac_01 import Node
h=s()
def reverse_words():
    for i in text:
        if i==" ":
            while not h.isempty():
                print(h.head.data)
                h.pop()
        else:
            h.push(i)
text="hello hi"
reverse_words(text)