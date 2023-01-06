class KeyIndex:
  def __init__(self,lst):
    self.length = len(lst)
    flag = True
    for elm in lst:

      if elm <0:
        flag = False
        break
    self.flag = flag
    if flag:
      maxnum = lst[0]
      for elm in lst:
        if maxnum < elm:
          maxnum = elm
      
      self.auxarray = [0]*(maxnum+1)
      for elm in lst:
        self.auxarray[elm]+= 1
      print(self.auxarray)
    else:
      minnum = lst[0]
      
      for elm in lst:
        if elm < minnum:
          minnum = elm
      self.minnum = minnum
      maxnum = None
      for elm in range(len(lst)):
        lst[elm] = lst[elm] - minnum
        if maxnum == None:
          maxnum = lst[elm]
        elif lst[elm] > maxnum:
          maxnum = lst[elm]
      self.auxarray = [0]*(maxnum+1)
      for elm in lst:
        self.auxarray[elm]+= 1
      #print(self.auxarray)

  def search(self,elm):
    if self.flag == False:
      elm = elm - self.minnum
    if elm <len(self.auxarray):
      count = 0
      k = self.auxarray[elm]
      if k ==0:
        return False
      else:
        return True
    else:
      return False

  def sort(self):
    lst = [0]*self.length
    count = 0
    for i in range(len(self.auxarray)):
      elm = self.auxarray[i]
      for j in range(elm):
        lst[count] = i + self.minnum
        count += 1
    return lst


lst = [-9,6,12,5,6,12,-1]

s = KeyIndex(lst)
print(s.search(5))
print(s.sort())