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


      

