def func(num,current=1):
    if num == current:
        return 1/num 
    else:
        return 1/current + func(num,current+1)

print(func(7))


class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next
        
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self,elm):
        if self.head == None:
            self.head = Node(elm,None)
            
        else:
            k = Node(elm,self.head)
            
            self.head = k
    def pop(self,elm):
        if self.head == None:
            print("overflow")
        else:
            print(self.head.val)
            self.head = self.head.next

s = Stack()
for elm in range(10):
    s.push(elm)

for elm in range(10):
    s.pop(elm)




