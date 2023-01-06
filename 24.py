class CircularArray:
  def __init__(self, lin, st, sz):
    # Initializing Variables
    self.lin= lin
    self.start = st
    self.size = sz
    self.cir = [None]*len(lin)
    for index in range(self.size):
      new =(self.start+index)%len(lin)
      self.cir[new]=lin[index]

  # Print from index 0 to len(cir) - 1
  def printFullLinear(self):
    for index in range(len(self.cir)):

      if index == len(self.cir)-1:
        print(self.cir[index])

      else:
        print(self.cir[index],end=", ")

  # Print from start index and total size elements
  def printForward(self):
    for index in range(self.size):
      for_ind=(self.start+index)%len(self.cir)
      if index == self.size-1:
        print(self.cir[for_ind])

      else:
        print(self.cir[for_ind],end=", ")


  def printBackward(self): #Easy
    for index in range((self.size-1),-1,-1):
      back_ind = (self.start+index)%len(self.cir)
      if index == 0:
        print(self.cir[back_ind])

      else:
        print(self.cir[back_ind],end=", ")


  # With no null cells
  def linearize(self):
    space=[None]*self.size
    
    for index in range(self.size):
      count = (self.start+index)%len(self.cir)
      space[index]=self.cir[count]

    self.cir = space

  # Do not change the Start index
  def resizeStartUnchanged(self, newcapacity):
    space =[None]*newcapacity
    for index in range(self.size):
      new_ind = (index + self.start)% (newcapacity)
      cir_ind = (index+self.start)%len(self.cir)
      space[new_ind]=self.cir[cir_ind]

    self.cir=space

  def palindromeCheck(self):
    flag = 1
    index = 0
    last_index = self.size-1
    while index < (self.size-1)//2:
      begin = (self.start + index)%len(self.cir)
      end = (self.start+last_index)%len(self.cir)
      index+=1
      last_index-=1
      if self.cir[begin]!=self.cir[end]:
        flag = 0
        break

    if flag == 1:
      print("This array is a palindrome")
    else:
      print("This array is not a palindrome")

    


  def sort(self):
    space=[None]*self.size
    
    for index in range(self.size):
      count = (self.start+index)%len(self.cir)
      space[index]=self.cir[count]

    self.cir = space
    
    for ind in range(self.size-1):
        for indx in range(self.size-1):
            if self.cir[indx]>self.cir[indx+1]:
                temp = self.cir[indx]
                self.cir[indx] = self.cir[indx+1]
                self.cir[indx+1] = temp

    gg = [None]*len(self.cir)
    for index in range(self.size):
      new =(self.start+index)%len(self.cir)
      gg[new]=self.cir[index]

    self.cir = gg


  def equivalent(self, cir_arr):
    flag = True
    
    if self.size!=cir_arr.size:
      flag= False

    else:
      for index in range(self.size):
        one = (self.start+ index)%len(self.cir)
        two = (cir_arr.start+index)%len(cir_arr.cir)
        if self.cir[one]!=cir_arr.cir[two]:
          flag = False
          break

    return flag

  def intersection(self, c2):
    x = 0
    if self.size < c2.size:
      new = [None]*c2.size
    else:
      new = [None]*self.size



    
    for index in range(self.size):
      one = (self.start+index)%len(self.cir)
      for indx in range(c2.size):
        two = (c2.start+indx)%len(c2.cir)
        
        if self.cir[one]==c2.cir[two]:
            count = 0
            for ind in range(len(new)):
                if new[ind] == self.cir[one]:
                    count += 1
            if count <1:
                new[x] = self.cir[one]
                x = x +1
                #print("YO")
                break
    j = 0
    for i in range(len(new)):
        if new[i] != None:
            j += 1
    xyz = [None]*j
    for i in range(j):
        xyz[i] = new[i]


                    
    return xyz
               




    
      

# Tester class. Run this cell after completing methods in the upper cell and
# check the output

lin_arr1 = [10, 20, 30, 40, None]

print("==========Test 1==========")
c1 = CircularArray(lin_arr1, 2, 4)
c1.printFullLinear() # This should print: 40, None, 10, 20, 30
c1.printForward() # This should print: 10, 20, 30, 40
c1.printBackward() # This should print: 40, 30, 20, 10

print("==========Test 2==========")
c1.linearize()
c1.printFullLinear() # This should print: 10, 20, 30, 40


print("==========Test 3==========")
lin_arr2 = [10, 20, 30, 40, 50]
c2 = CircularArray(lin_arr2, 2, 5)
c2.printFullLinear() # This should print: 40, 50, 10, 20, 30
c2.resizeStartUnchanged(8) # parameter --> new Capacity
c2.printFullLinear() # This should print: None, None, 10, 20, 30, 40, 50, None

print("==========Test 4==========")
lin_arr3 = [10, 20, 30, 20, 10, None, None]
c3 = CircularArray(lin_arr3, 3, 5)
c3.printForward() # This should print: 10, 20, 30, 20, 10
c3.palindromeCheck() # This should print: This array is a palindrome

print("==========Test 5==========")
lin_arr4 = [10, 20, 30, 20, None, None, None]
c4 = CircularArray(lin_arr4, 3, 4)
c4.printForward() # This should print: 10, 20, 30, 20
c4.palindromeCheck() # This should print: This array is NOT a palindrome

print("==========Test 6==========")
lin_arr5 = [10, 20, -30, 20, 50, 30, None]
c5 = CircularArray(lin_arr5, 5, 6)
c5.printForward() # This should print: 10, 20, -30, 20, 50, 30
c5.sort()
c5.printForward() # This should print: -30, 10, 20, 20, 30, 50

print("==========Test 7==========")
lin_arr6 = [10, 20, -30, 20, 50, 30, None]
c6 = CircularArray(lin_arr6, 2, 6)
c7 = CircularArray(lin_arr6, 5, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c7.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c7)) # This should print: True

print("==========Test 8==========")
lin_arr7 = [10, 20, -30, 20, 50, 30, None, None, None]
c8 = CircularArray(lin_arr7, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c8.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c8)) # This should print: True

print("==========Test 9==========")
lin_arr8 = [10, 20, 30, 40, 50, 60, None, None, None]
c9 = CircularArray(lin_arr8, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c9.printForward() # This should print: 10, 20, 30, 40, 50, 60
print(c6.equivalent(c9)) # This should print: False

print("==========Test 10==========")
lin_arr9 = [10, 20, 30, 40, 50,10, None, None, None]
c10 = CircularArray(lin_arr9, 5, 6)
c10.printFullLinear() # This should print: 40, 50, None, None, None, 10, 20, 30
lin_arr10 = [5, 40, 15, 25, 10, 20, 5,10, None, None, None, None, None]
c11 = CircularArray(lin_arr10, 8, 8)
c11.printFullLinear() # This should print: 10, 20, 5, None, None, None, None, None, 5, 40, 15, 25
output = c10.intersection(c11)
print(output) # This should print: [10, 20, 40]


