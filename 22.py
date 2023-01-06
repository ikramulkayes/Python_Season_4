#Task1
def shiftLeft(lst,k):
  lenlst = len(lst)
  for elm in range(0,len(lst)):
    if elm < (lenlst-k):
      lst[elm] = lst[elm+k]
    else:
      lst[elm] = 0
 

  
  return lst

print(shiftLeft([10,20,30,40,50,60],1))