#dummy headed
#Cell one
class Node:
  def __init__(self, e, n, p):
    self.element = e
    self.next = n
    self.prev = p

class DoublyList:
  
  def __init__(self, a):
  #  Design the constructor based on data type of a. If 'a' is built in python list then
  #  Creates a linked list using the values from the given array.
    if type(a) == list:
      self.head = Node(None,None,None)
      tail = self.head
      for elm in range(0,len(a)):
        obj = Node(a[elm],None,None)
        tail.next = obj
        obj.prev = tail
        tail = obj
      tail.next= self.head
      self.head.prev = tail  
      self.tail = tail
    else:
      self.head = a
      self.tail = self.head.prev

  
  # Counts the number of Nodes in the list
  def countNode(self):
    count = 0
    obj = self.head.next
    while obj != self.head:
      count += 1
      obj = obj.next
    return count
  def rotateleft(self,k):
    for elm in range(k):
        temp = self.head.next.element
        obj = self.head.next
        while obj.next.element != None:
            obj.element = obj.next.element
            obj = obj.next
        obj.element = temp

  def forwardprint(self):
    #print(str(self.head.element)+", ",end="")
    obj = self.head.next
    while obj != self.head:
        if obj.next != self.head:
            print(str(obj.element)+", ",end="")
        else:
            print(obj.element)
        obj = obj.next
  def rotateright(self,k):
    for elm in range(k):
        temp = self.head.next.element
        obj = self.head.next.next
        while obj != self.head:
            k = obj.element
            obj.element = temp
            temp = k
            obj = obj.next
        self.head.next.element = temp 
  def palindrome_check(self):
    obj = self.head.next
    while obj.next != self.head:
        obj = obj.next
    tail = obj
    obj = self.head.next
    idx = self.countNode()
    idx = idx//2
    flag = True
    for i in range(idx):
        #print(obj.element,tail.element)
        if obj.element != tail.element:
            flag = False
            break
        obj = obj.next
        tail = tail.prev
    return flag
  def merge(self,other):
    count = 0
    head = Node(None, None, None)
    tail = head
    obj1 = self.head.next
    while obj1 != self.head:
      obj = Node(obj1.element, None, tail)
      tail.next = obj
      tail = obj
      count +=1
      obj1 = obj1.next
    obj2 = other.head.next
    while obj2 != other.head:
      obj = Node(obj2.element, None, tail)
      tail.next = obj
      tail = obj 
      count += 1
      obj2 = obj2.next
    tail.next = head
    head.prev = tail
    obj1 = head.next
    obj2 = obj1.next
    #print("YO")
    for i in range(count):
      obj1 = head.next
      obj2 = obj1.next
      
      for j in range(count-i-1):
        if obj1.element > obj2.element:
          temp = obj1.element
          obj1.element = obj2.element
          obj2.element = temp
        obj1 = obj1.next
        obj2 = obj2.next
    return head
  def prev_insert(self,idx,val):
    obj = self.head.next
    tail = self.head
    count = 1
    while obj != self.head:

      if idx == count:
        gg = Node(val, obj, tail)
        tail.next = gg
        obj.prev = gg
        break
      #print(count)
      tail = obj
      obj = obj.next
      count += 1
    if count == idx:
        gg = Node(val, obj, tail)
        tail.next = gg
        obj.prev = gg
  
        




     


    





lst1 = [1,1,2,9]
lst2 = [2,4,5,7]
s1 = DoublyList(lst1)
s2 = DoublyList(lst2)

s1.forwardprint()
s2.forwardprint()
#s.rotateleft(20)
#s.rotateright(601)
#s = s1.merge(s2)
#k = DoublyList(s)
#k.forwardprint()
s1.prev_insert(1, 99)
s1.forwardprint()








