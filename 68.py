def binary_searching(lst,val,low=None,high=None):
    if low == None:
        low = 0
        high = len(lst)-1
    
    
    print(low,high)
    mid = (low + high)//2
    if lst[mid] == val:
       return "Found"
    elif low == high:
        return "Not found"


    elif lst[mid]<= val:
        low = mid+1
    elif lst[mid] > val:
        high = mid
    

    return binary_searching(lst, val, low, high)


lst = [1,2,3,4,5,6,7,8,9]
print(binary_searching(lst, 9))
    
def binary_searching(lst,elm,low=0,high=None):
    if high == None:
        high = len(lst)-1
    mid = (low+high)//2
    if elm == lst[mid]:
        return mid
    elif low == high:
        return "Not found"
    elif lst[mid]>elm:
        
        return binary_searching(lst, elm,low,mid)
    else:
        return binary_searching(lst, elm,mid+1,high)

lst = [1,2,3,4,5,6]      
#print(binary_searching(lst, 6))