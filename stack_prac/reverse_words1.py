from prac_01 import stack as s
from prac_01 import Node
h=s()
def reverse_words(text):
    for i in text:
        if i==" ":
            while not h.isempty():
                print(h.head.data)
                h.pop()
            print(" ")
        else:
            h.push(i)
        
    while not h.isempty():
        print(h.head.data)
        h.pop()
    print(" ")   
text="hello hi good morning"
reverse_words(text)