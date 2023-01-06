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
  
  # prints the elements in the list
  def forwardprint(self):
    #print(str(self.head.element)+", ",end="")
    obj = self.head.next
    while obj != self.head:
        if obj.next != self.head:
            print(str(obj.element)+", ",end="")
        else:
            print(obj.element)
        obj = obj.next
    

  # prints the elements in the list backward
  def backwardprint(self):
    print(str(self.tail.element)+", ",end="")
    obj = self.tail.prev
    while obj != self.tail:
        if obj.prev != self.tail and obj.prev.element != None :
            print(str(obj.element)+", ",end="")
        else:
            print(obj.element)
            break
        obj = obj.prev   

  # returns the reference of the at the given index. For invalid index return None.
  def nodeAt(self, idx):
    count =0
    obj = self.head.next
    if idx <0:
      return Node("index error",None,None)
    while obj != self.head:
      if idx == count:
        return obj
      obj = obj.next
      count += 1
    return Node("index error",None,None)
  
  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    count =0
    obj = self.head.next

    while obj != self.head:
      if obj.element == elem:
        return count
      obj = obj.next
      count += 1
    return -1

  # inserts containing the given element at the given index Check validity of index. 
  def insert(self, elem, idx):
    obj = self.head
    obj = obj.next
    count = 0
    flag = True
    if idx <0:
      print("Insert proper index")
      return
    while obj != self.head:
      if count == idx:
        newobj = Node(elem, obj, obj.prev)
        temp = obj.prev
        obj.prev = newobj
        temp.next = newobj
        flag = False
        break
      count+=1
      obj = obj.next
    if count == idx and flag:
      newobj = Node(elem, self.head, self.tail)
      self.tail.next = newobj
      self.head.prev = newobj
      self.tail = newobj
      flag = False
    if flag == True:
      print("Insert proper index")
      return 
        
        
        


    
  # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
  def remove(self, idx):
    obj = self.head
    obj = obj.next
    count = 0
    flag = True
    if idx <0:
      return None
    while obj != self.head:
      if idx == count:
        temp = obj.element
        prevobj = obj.prev
        nextobj = obj.next
        prevobj.next = nextobj
        nextobj.prev = prevobj
        if obj == self.tail:
          self.tail = prevobj
        return str(temp)
      obj = obj.next
      count += 1   
    return None


print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

h1.forwardprint() # This should print: 10,20,30,40. 
h1.backwardprint() # This should print: 40,30,20,10. 
print(h1.countNode()) # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.  

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,85.  

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85. 


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.  

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.