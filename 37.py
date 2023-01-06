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



class Solution:
    def nextGreaterElement(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        flst = []
        for elm1 in nums1:
          count = 0
          for elm2 in nums2:
            
            if elm1 == elm2:
              break
            count += 1
          flag = True
          #print(count)
          for i in range(count,len(nums2)):
            
            if nums2[i] > elm1:
              flst.append(nums2[i])
              flag = False
              break
          if flag:
            flst.append(-1)
          
          

            


            
        return flst
        
s = Solution()
print((s.nextGreaterElement([2,1,4], [1,2,3,4])))