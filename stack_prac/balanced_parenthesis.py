from prac_01 import stack as s
#from prac_01 import Node
h=s()
def check_balanced_parenthesis(text):
    for i in text:
        if i =="(":
            h.push(i)
        elif i==')':
            if h.peek()!='(':
                print("not balanced")
                break
            else:
                h.pop()
    if not h.isempty():
        print("not balanced")
    else:
        if(i==(text[-1])):
            print("balanced")
         
text="(())"
check_balanced_parenthesis(text)