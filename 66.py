def insertionsort(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i -1
        while lst[j] > key and j >=0:
            lst[j+1] = lst[j]
            j -= 1
        lst[j + 1] = key
    print(lst)

lst = [11,5,6,2,3]
insertionsort(lst)

class recinsertion:
    def __init__(self,lst):
        self.lst = lst
    def iterate(self,index = 0):
        if index >= len(self.lst):
            return self.lst
        else:
            j = index -1
            key = self.lst[index]
            self.func1(j,key)
            index += 1
            return self.iterate(index)

    def func1(self,j,key):
        if self.lst[j] > key and j >= 0:
            self.lst[j+1] = self.lst[j]
            j -= 1
            self.func1(j,key)
        else:
             self.lst[j+1] = key

s = recinsertion(lst)
print(s.iterate())
