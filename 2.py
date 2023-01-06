
#Task 7
def splittingArray(lst):
    
    
    for belm in range(1,len(lst)):
        sum1 = 0
        sum2 = 0
        for elm in range(belm):
            
            sum1 += lst[elm]
        
        for elm in range(belm,len(lst)):
            
            sum2 += lst[elm]
        
        if sum1 == sum2:
            return True
    return False

lst = [10, 3, 1, 2, 10]
print(splittingArray(lst))

