class Node:
    def __init__(self,val,next):
        self.elm = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.count = None
    def push(self,val):
        if self.head == None:
            self.head = Node(val, None)
            self.count = 0
        else:
            temp = Node(val,self.head)
            self.head = temp
            self.count += 1
    def pop(self):
        if self.count <0:
            print("Overflow")
        else:
            temp = self.head
            self.head = self.head.next
            self.count -= 1
            return temp.elm
word = input()
s = Stack()
for elm in word:
    s.push(elm)
flag = True



for elm in range(len(word)//2):
    
    
    gg = s.pop()
    #print(gg,word[elm])
    if gg == word[elm]:
        pass
    else:
        print("Not palindrome")
        flag = False
        break
if flag:
    print("Palindrome")



