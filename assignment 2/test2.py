class CircularArray:
  def __init__(self, lin, st, sz):
    # Initializing Variables
    self.start = st
    self.size = sz
    self.cir = [None]*len(lin)
    k = st
    for elm in range(self.size):
      self.cir[k] = lin[elm]
      k += 1
      k = k%len(lin)
    


    
    # if lin = [10, 20, 30, 40, None]
    # then, CircularArray(lin, 2, 4) will generate
    # cir = [40, null, 10, 20, 30]
    
    # To Do. 
    # Hints: set the values for initialized variables
  
  # Print from index 0 to len(cir) - 1
  def printFullLinear(self): #Easy
    
    for elm in range(len(self.cir)):
      if elm == len(self.cir)-1:
        print(self.cir[elm])
      else:
        print(str(self.cir[elm])+", ",end="")



  
  # Print from start index and total size elements
  def printForward(self): #Easy
    k = self.start
    for elm in range(self.size):
      if elm == self.size-1:
        print(self.cir[k])
      else:
        print(str(self.cir[k])+", ",end="")
      k += 1
      k = k%len(self.cir)

  
  def printBackward(self): #Easy
    self.end = self.start + self.size -1
    self.end = self.end%len(self.cir)
    k = self.end

    for elm in range(self.size):
      #print(k)
      if elm == self.size-1:
        print(self.cir[k])
      else:
        print(str(self.cir[k])+", ",end="")
      k -= 1
      if k == -1:
        k = len(self.cir)-1      
  
  # With no null cells
  def linearize(self): #Medium
    lst = [None]*self.size
    k = self.start
    for elm in range(self.size):
      lst[elm] = self.cir[k]
      k += 1
      k = k%len(self.cir)
    self.cir = lst
  
  # Do not change the Start index
  def resizeStartUnchanged(self, newcapacity): #Medium
    lst = [None]*newcapacity
    k = self.start
    l = self.start
    for elm in range(self.size):
      lst[l] = self.cir[k]
      k += 1
      k = k% len(self.cir)

      l += 1
      l = l %len(lst)
    self.cir = lst

  
  # This method will check whether the array is palindrome or not
  def palindromeCheck(self): #Hard
    start = self.start
    end = self.start + self.size -1
    end = end % len(self.cir)
    flag = True
    for elm in range(self.size):
      if self.cir[start] != self.cir[end]:
        print("This should print: This array is NOT a palindrome")
        flag = False
        break
      start += 1
      start = start % len(self.cir)

      end -= 1
      if end == -1:
        end = len(self.cir)-1
    if flag:
      print("This should print: This array is a palindrome")



      

  # This method will sort the values by keeping the start unchanged
  def sort(self):
    for elm in range(self.size-1):
      for selm in range(self.size-elm-1):
        selm += self.start
        selm = selm % len(self.cir)
        end = (selm+1)%len(self.cir)
        if self.cir[selm] > self.cir[end]:
          temp = self.cir[selm]
          self.cir[selm] = self.cir[end]
          self.cir[end] = temp
  

  
  # This method will check the given array across the base array and if they are equivalent interms of values return true, or else return false
  def equivalent(self, cir_arr):
    flag = True
    start1 = self.start
    start2 = cir_arr.start
    if self.size == cir_arr.size:
      for elm in range(self.size):
        if self.cir[start1] != cir_arr.cir[start2]:
          return False
        start1 = (start1+1)%len(self.cir)
        start2 = (start2+1)%len(cir_arr.cir)
    else:
      return False
    return True



  # the method take another circular array and returns a linear array containing the common elements between the two circular arrays.
  def intersection(self, c2): 
    lst1 = self.cir
    lst2 = c2.cir
    index1 = self.start
    index2 = c2.start
    if self.size >= c2.size:
      final = [None]*self.size
    else:
      final = [None]*c2.size
    finalcount = 0
    size1 = self.size
    size2 = c2.size
    tempindex2 = index2
    for i in range(size1):
      index2 = tempindex2
      var1 = lst1[index1]
      flag = False
      for j in range(size2):
        var2 = lst2[index2]
        if var1 == var2 and var1 != None and var2 != None:
          flag = True
          
          j = index2
          for elm in range(size2):
            
            j = j %(len(lst2))
            k = (j+1)%(len(lst2))
            lst2[j] = lst2[k]
            j = k
            if lst2[j] == None:
              break
          size2 -= 1

          for elm in final:
            if elm == var1:
              flag = False
              break
          if flag:
            final[finalcount] = var1
            finalcount += 1
            break
        index2 += 1
        index2 = index2%len(lst2)
      index1 += 1
      index1 = index1%len(lst1)
    result = [None]*(finalcount)
    for elm in range(finalcount):
      result[elm] = final[elm]
    #print(lst1)
    #print(lst2)
    return result
        













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
lin_arr4 = [10, 20, 20,10, None, None, None]
c4 = CircularArray(lin_arr4, 3, 4)
c4.printForward() # This should print: 10, 20, 30, 20
c4.palindromeCheck() # This should print: This array is NOT a palindrome

print("==========Test 6==========")
lin_arr5 = [10, 10, 10, 10, 10, 110, None]
c5 = CircularArray(lin_arr5, 5, 6)
c5.printForward() # This should print: 10, 20, -30, 20, 50, 30
c5.sort()
c5.printForward() # This should print: -30, 10, 20, 20, 30, 50

print("==========Test 7==========")
lin_arr6 = [10, 20, -30, 20, 50, 30,99, None]
c6 = CircularArray(lin_arr6, 2, 7)
c7 = CircularArray(lin_arr6, 5, 7)
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
lin_arr9 = [10, 20, 30, 40, 50,30,30,20, None, None, None]
c10 = CircularArray(lin_arr9, 5, 8)
c10.printFullLinear() # This should print: 40, 50, None, None, None, 10, 20, 30
lin_arr10 = [5, 40, 15, 25, 10, 20, 5,40, None, None, None, None, None]
c11 = CircularArray(lin_arr10, 8, 8)
c11.printFullLinear() # This should print: 10, 20, 5, None, None, None, None, None, 5, 40, 15, 25
output = c10.intersection(c11)
print(output) # This should print: [10, 20, 40]