class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n
    
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



class Stackobj:
  def __init__(self,element,idx):
    self.element = element
    self.idx1 = idx




word = "1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
s = Stack()
flag1 = True
flag2 = True
count =0


for i in word:
  elm = Stackobj(i,count)
  k = s.head

  
  if elm.element == "(" or elm.element== "{" or elm.element== "[":
    s.push(elm)
    
    
  elif elm.element == ")" or elm.element== "}" or elm.element== "]": 
    if s.isEmpty() == False:
      
      temp = s.pop()
      
      if elm.element == ")":
        if temp.element == "(":
          pass
        else:
          flag1 = False
          break
      elif elm.element =="}":
        if temp.element == "{":
          pass
        else:
          flag1 = False
          break
      elif elm.element == "]":
        if temp.element == "[":
          pass
        else:
          flag1 = False
          break
    else:
      temp = elm
      flag1 = False
      break
  count += 1

if s.isEmpty == False:
  #print("YO")
  flag1 = False

if flag1:
  print("Equation is alright")
else:
  if temp.element == "(" or temp.element== "{" or temp.element== "[":
    openclose = "closed"
  else:
    openclose = "opened"
  print("This expression is NOT correct.")
  print(f"Error at character # {temp.idx1+1}. ‘{temp.element}‘- not {openclose}.")


