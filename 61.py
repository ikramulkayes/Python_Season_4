class KeyIndex:
    def __init__(self, a):
        self.a = a
        max_temp = a[0]
        min_temp = a[0]
        flag = True
        for p in range(len(a)):
            if a[p] < 0:
                flag = False
            else:
                flag = True
        self.flag = flag        
        if flag == True:
            for i in range(1, len(a)):     
                if a[i] > max_temp:
                    max_temp = a[i]
            self.k = [None]*(max_temp+1)
        
            for elm in self.a:
                if self.k[elm] == None:
                    self.k[elm] = 1
                else:
                    self.k[elm] += 1
        else:
            for i in range(1, len(a)):     
                if a[i] > max_temp:
                    max_temp = a[i]
                if a[i] < min_temp:
                    min_temp = a[i]
            for i in range(len(a)):
                a[i] = a[i]-min_temp
            self.min_temp = min_temp
            max_temp = max_temp - min_temp
            self.k = [None]*(max_temp+1)
            for elm in self.a:
                if self.k[elm] == None:
                    self.k[elm] = 1
                else:
                    self.k[elm] += 1
        self.max_temp = max_temp
                     
            
                    
                    
    def srch_value(self, val):
        flag = self.flag
        if flag:
            if val < len(self.k):
                temp = self.k[val]
                #print(temp)
                if temp == None:
                    return False
                else:
                    return True
            else:
                return False
        else:
            if val <= self.max_temp and val >= self.min_temp:
                temp = self.k[val+self.min_temp]
                
                if temp == None:
                    return False
                else:
                    return True
            else:
                return False               

        
    def sort_print(self):
        pointer = 0
        if self.flag:
            for p in range(len(self.k)):
                if self.k[p] != None:
                    for i in range(self.k[p]):
                        print(p, end = ', ')
        else:
            for p in range(len(self.k)):
                if self.k[p] != None:
                    for i in range(self.k[p]):
                        print(p+self.min_temp, end = ', ')
           

    
    
a1 = KeyIndex([-10, 4, 5, 4, -10, 2, 2, 9,-1])
print(a1.srch_value(1))
a1.sort_print()