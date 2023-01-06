def binary_searching(lst,elm):
    low = 0
    high = len(lst)-1
    
    while True:
        
        mid = (high +low)//2
        print(low,high,mid)
        if lst[mid] == elm:
            return mid
        elif high == low:
            return "Not found"
        elif lst[mid] > elm:
            high = mid
        else:
            low = mid+1


lst = [1,2,3,4,5,6]      
print(binary_searching(lst, 6))