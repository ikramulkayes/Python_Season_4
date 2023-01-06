class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n

class QNode:
    def __init__(self,e,n,j):
        self.element = e
        self.next = n
        self.prev = j
    
class Stack:
  def __init__(self):
    self.head = None
    self.length = 0
  def push(self,elm):
    if self.head== None:
      self.head = Node(elm,None)
      self.length+= 1

    else:
      tempnode = Node(elm,self.head)
      self.head = tempnode
      self.length += 1
  def pop(self):
    if self.head == None:
      print("Underflow")
    else:
      temp = self.head.element
      self.head = self.head.next
      self.length -= 1
      return temp
  def isEmpty(self):
    if self.length == 0:
      return True
    else:
      return False

class Quee:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  def push(self,elm):
    if self.head== None:
      self.head = QNode(elm,None,None)
      self.tail = self.head
      self.length+= 1

    else:
      tempnode = QNode(elm,None,self.head)
      self.tail.next = tempnode
      self.tail = tempnode
      self.length += 1
  def pop(self):
    if self.head == None:
      print("Underflow")
    else:
      temp = self.head.element
      self.head = self.head.next
      self.length -= 1
      return temp
  def isEmpty(self):
    if self.length == 0:
      return True
    else:
      return False

s = Quee()
l = Stack()
lst1 =    [1,1,0,0]
lst2 =    [0,1,0,1] 
lst2 = lst2[::-1] # as to make the situation according to question
for elm in lst1:
    #s.push(elm)
    s.push(elm)

for elm in lst2:
    
    #print(s.pop())
    #print(l.pop())
    l.push(elm)
count = 0

while l.isEmpty() != True:
    student = s.pop()
    
    burger = l.pop()
    #print(student,burger)
    if count > l.length:
      s.push(student)
      l.push(burger)      
      break
    if student != burger:
        s.push(student)
        l.push(burger)
        count += 1
    else:
      count = 0

count =0
while s.isEmpty() != True:
  s.pop()
  count += 1
print(count)





