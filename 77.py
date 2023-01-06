lst = [None]*9
class Quee:
    def __init__(self):
        self.count = 0
        self.end = None
    def enquee(self,lst,start,val):
        if self.end == None:
            self.end = start
        lst[self.end] = val
        self.end += 1
        self.count += 1
        
        print(lst)
    def dequee(self,lst,start):
        for elm in range(self.count-1):
            lst[(start + elm)%len(lst)] = lst[(start + elm +1)%len(lst)]
        lst[start + self.count-1] = None
        print(lst)
        self.count -= 1
        self.end -= 1
        if self.end <0:
            self.end = len(lst) -1 

s = Quee()
s.enquee(lst, 2, 1)
s.enquee(lst, 2, 2)
s.enquee(lst, 2, 3)
s.dequee(lst, 2)
s.dequee(lst, 2)
s.enquee(lst, 2, 1)
s.enquee(lst, 2, 10)
