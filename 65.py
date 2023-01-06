def ordvalue(word,index=0):
    sum1 = ord(word[index])
    index += 1
    if index >= len(word):
        return sum1
    else:
        
        return sum1+ ordvalue(word,index)

class hashmap:
    def __init__(self):
        self.flst = [None]*9
    def lst_iterate(self,lst,index=0):
        if index >=len(lst):
            return self.flst
        else:
            val = ordvalue(lst[index])%9
            print(val)
            self.hash_iterate(lst[index],val)
            index += 1
            return self.lst_iterate(lst,index)
    
    def hash_iterate(self,elm,index,count = 0):
        
        if count >= 9:
            print("Hash full")
        elif self.flst[index] == None:
            self.flst[index] = elm
        else:
            count += 1
            index = (index+1)%9
            self.hash_iterate(elm, index,count)

lst = ["baby","mouly","fahad","mouly"]
s = hashmap()
s.lst_iterate(lst)
print(s.flst)
        
