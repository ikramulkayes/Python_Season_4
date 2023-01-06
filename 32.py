class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n




class LinkedList:
  
  def __init__(self, a):
  #  Design the constructor based on data type of a. If 'a' is built in python list then
  #  Creates a linked list using the values from the given array. head will refer
  #  to the Node that contains the element from a[0]
  #  Else Sets the value of head. head will refer
  # to the given LinkedList

  # Hint: Use the type() function to determine the data type of a
    if type(a) == list:
      self.head = Node(a[0],None)
      tail = self.head
      for elm in range(1,len(a)):
        obj = Node(a[elm],None)
        tail.next = obj
        tail = obj
    else:
      self.head = a
      


  
  # Count the number of nodes in the list
  def countNode(self):
    obj = self.head
    count = 0
    while obj != None:
      count += 1
      obj = obj.next
    return count


  
  # Print elements in the list
  def printList(self):
    obj = self.head
    while obj != None:
      if obj.next == None:
        print(str(obj.element))
      else:
        print(str(obj.element)+",",end="")
      obj = obj.next
    

  # returns the reference of the Node at the given index. For invalid index return None.
  def nodeAt(self, idx):
    count = 0
    obj = self.head
    while obj!= None:
      if count==idx:
        return obj
      obj = obj.next
      count += 1
    raise IndexError
  
  # returns the element of the Node at the given index. For invalid idx return None.
  def get(self, idx):
    count = 0
    obj = self.head
    while obj!= None:
      if count==idx:
        return obj.element
      obj = obj.next
      count += 1
  
  # updates the element of the Node at the given index. 
  # Returns the old element that was replaced. For invalid index return None.
  # parameter: index, element
  def set(self, idx, elem):
    obj = self.head
    count = 0
    while obj != None:
      if count == idx:
        temp = obj.element
        obj.element = elem
        return temp
      obj = obj.next
      count += 1
    return None

  # returns the index of the Node containing the given element.
  # if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    count = 0
    obj = self.head
    while obj!= None:
      if obj.element==elem:
        return count
      obj = obj.next
      count += 1
    return -1
  # returns true if the element exists in the List, return false otherwise.
  
  def contains(self, elem):
    
    obj = self.head
    while obj!= None:
      if obj.element==elem:
        return True
      obj = obj.next
    return False
      
    return -1

  # Makes a duplicate copy of the given List. Returns the reference of the duplicate list.
  def copyList(self):
    # To Do
    
    
    head = Node(self.head.element,None)
    obj2 = self.head
    tail = head
    while obj2.next != None:
      tail.next = Node(obj2.next.element,None)
      tail = tail.next
      obj2 = obj2.next
    return head


  # Makes a reversed copy of the given List. Returns the head reference of the reversed list.
  def reverseList(self):
    
    obj1 = self.head
    obj2 = obj1.next
    obj1.next = None
    tail = obj1
    while obj2 != None:
      temp = obj2.next
      obj2.next = tail
      tail = obj2
      obj2 = temp
    return tail
    #print(tail.element)
    #print(tail.next.element)

      
      


  
  # inserts Node containing the given element at the given index
  # Check validity of index.
  def insert(self, elem, idx):
    obj1 = self.head
    count = 0
    tail = None
    while obj1 != None:
      if count == idx:
        obj = Node(elem,obj1)

        if tail != None:
          tail.next = obj
        else:
          self.head = obj
      tail = obj1
      obj1 = obj1.next
      count += 1
    if count == idx:
      tail.next = Node(elem,None)






  # removes Node at the given index. returns element of the removed node.
  # Check validity of index. return None if index is invalid.
  def remove(self, idx):
    # To Do
    obj = self.head
    count = 0
    tail = None
    
    if count < 0:
      return None
    while obj != None:
      if count == idx:
        if count ==0:
          self.head = self.head.next
          return obj.element
        else:
          
          tail.next = obj.next
          return obj.element
      tail = obj
      obj = obj.next
      count += 1

  
  # Rotates the list to the left by 1 position.
  def rotateLeft(self):
    temp = self.head.element
    obj2 = self.head.next
    obj1 = self.head
    
    while obj2 != None:
      obj1.element = obj2.element
      obj1 = obj1.next
      obj2 = obj2.next
    obj1.element = temp


      

  
  
  # Rotates the list to the right by 1 position.
  def rotateRight(self):
    
    obj1 = self.head
    ftemp = obj1.element
    while obj1.next != None:
      temp = obj1.next.element
      obj1.next.element = ftemp
      ftemp = temp
      obj1 = obj1.next
    self.head.element = ftemp


print("////// Test 01 //////")
a1 = [10, 20, 30, 40]
h1 = LinkedList(a1) # Creates a linked list using the values from the array
# head will refer to the Node that contains the element from a[0]

h1.printList() # This should print: 10,20,30,40
print(h1.countNode()) # This should print: 4

print("////// Test 02 //////")
# returns the reference of the Node at the given index. For invalid idx return None.
myNode = h1.nodeAt(1)
print(myNode.element) # This should print: 20. In case of invalid index This will generate an Error.
    
print("////// Test 03 //////")
# returns the element of the Node at the given index. For invalid idx return None.
val = h1.get(2)
print(val) # This should print: 30. In case of invalid index This will print None.
    
    
print("////// Test 04 //////")
    
# updates the element of the Node at the given index. 
# Returns the old element that was replaced. For invalid index return None.
# parameter: index, element
         
print(h1.set(1,85)) # This should print: 20
h1.printList() # This should print: 10,85,30,40.
print(h1.set(15,85)) # This should print: None
h1.printList() # This should print: 10,85,30,40. 
    
print("////// Test 05 //////")
# returns the index of the Node containing the given element.
# if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that doesn't exists in the list this will print -1.
    
print("////// Test 06 //////")
# returns true if the element exists in the List, return false otherwise.
ask = h1.contains(40)
print(ask) # This should print: True.
    
    
print("////// Test 07 //////")
a2 = [10,20,30,40,50,60,70]
h2 = LinkedList(a2) # uses theconstructor where a is an built in list
h2.printList() # This should print: 10,20,30,40,50,60,70.  
# Makes a duplicate copy of the given List. Returns the head reference of the duplicate list.
copyH=h2.copyList() # Head node reference of the duplicate list
h3 = LinkedList(copyH) # uses the constructor where a is head of a linkedlist 
h3.printList() # This should print: 10,20,30,40,50,60,70.  
    
print("////// Test 08 //////")
a4 = [10,20,30,40,50]
h4 = LinkedList(a4) # uses theconstructor where a is an built in list
h4.printList() # This should print: 10,20,30,40,50.  
# Makes a reversed copy of the given List. Returns the head reference of the reversed list.
revH=h4.reverseList() # Head node reference of the reversed list
h5 = LinkedList(revH) # uses the constructor where a is head of a linkedlist 
h5.printList() # This should print: 50,40,30,20,10.  
    
print("////// Test 09 //////")
a6 = [10,20,30,40]
h6 = LinkedList(a6) # uses theconstructor where a is an built in list
h6.printList() # This should print: 10,20,30,40.  
    
# inserts Node containing the given element at the given index. Check validity of index.
h6.insert(85,0)
h6.printList() # This should print: 85,10,20,30,40.  
h6.insert(95,3)
h6.printList() # This should print: 85,10,20,95,30,40.  
h6.insert(75,6)
h6.printList() # This should print: 85,10,20,95,30,40,75. 
    
    
    
print("////// Test 10 //////")
a7 = [10,20,30,40,50,60,70]
h7 = LinkedList(a7) # uses theconstructor where a is an built in list
h7.printList() # This should print: 10,20,30,40,50,60,70.  
    
# removes Node at the given index. returns element of the removed node.
# Check validity of index. return None if index is invalid.
    
print("Removed element:",h7.remove(0)) # This should print: Removed element: 10
h7.printList() # This should print: 20,30,40,50,60,70.  
print("Removed element: ",h7.remove(3)) # This should print: Removed element: 50
h7.printList() # This should print: 20,30,40,60,70.  
print("Removed element: ",h7.remove(4)) # This should print: Removed element: 70
h7.printList() # This should print: 20,30,40,60. 
    
    
print("////// Test 11 //////")
a8 = [10,20,30,40]
h8 = LinkedList(a8) # uses theconstructor where a is an built in list
h8.printList() # This should print: 10,20,30,40.  
    
# Rotates the list to the left by 1 position.
h8.rotateLeft()
h8.printList() # This should print: 20,30,40,10.  
    
    
print("////// Test 12 //////")
a9 = [10,20,30,40]
h9 = LinkedList(a9) # uses theconstructor where a is an built in list
h9.printList() # This should print: 10,20,30,40.  
    
# Rotates the list to the right by 1 position.
h9.rotateRight()
h9.printList() # This should print: 40,10,20,30.
