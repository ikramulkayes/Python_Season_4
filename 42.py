class Stack:
  def __init__(self,capacity):
    self.stack = [None]*capacity
    self.capacity = capacity
    self.idx = 0
  def push(self,element):
    if self.idx == self.capacity:
      print("Overflow")
      pass
    self.stack[self.idx] = element
    self.idx += 1
  def pop(self):
    temp = self.stack[self.idx-1]
    self.stack[self.idx-1] = None
    self.idx -=1
    return temp
  def isEmpty(self):
    if self.idx == 0:
      return False
    else:
      return True
class Stackobj:
  def __init__(self,element,idx):
    self.element = element
    self.idx1 = idx
word = input()   #input the equation here
s = Stack(10)
tempflag = True
flag = True
count = 0
for i in word:
  #print(s.stack)
  elm = Stackobj(i,count)
  
  if elm.element == "(" or elm.element== "{" or elm.element== "[":
    s.push(elm)
  elif elm.element == ")" or elm.element== "}" or elm.element== "]":
    if s.isEmpty():
      temp = s.pop()
      
      if elm.element == ")":
        if temp.element != "(":
          flag = False
          break
      elif elm.element == "}":
        if temp.element != "{":
          flag = False
          break
      elif elm.element == "]":
        if temp.element != "[":
          flag = False
          break
    else:
      temp = elm
      flag = False
      break
  count += 1
  #print(count)

if s.isEmpty() != False and flag == True:
  temp = s.pop()
  #print("YO")
  flag = False

if flag:
  print("This expression is correct.")
else:
  if temp.element == "(" or temp.element== "{" or temp.element== "[":
    openclose = "closed"
  else:
    openclose = "opened"
  print("This expression is NOT correct.")
  print(f"Error at character # {temp.idx1+1}. ‘{temp.element}‘- not {openclose}.")
for elm in s.stack:
  if elm == None:
    break
  #print(elm.element)