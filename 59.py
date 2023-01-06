class Hashfunction:
  def hash_string(self,part):
    a1 = 0
    a2 = 0
    for i in part:
      temp = ord(i)
      if temp >= 65 and temp <=90:
        if temp != 65 and temp != 69 and temp !=73 and temp != 79 and temp != 85:
          a1 += 1
          print(i)
      elif temp >= 48 and temp <= 57:
        a2 += int(i)
    return ((a1*24)+a2)%9
  def hash_table(self,array):
    new_array = [None]*9
    for i in array:
      a = self.hash_string(i)
      temp = a
      
      while new_array[temp] != None:
        temp = (temp+1)%9
      new_array[temp] = i
    return new_array

x = ["ST1E89B8A32"]
k = Hashfunction()
print(k.hash_table(x))     

    
