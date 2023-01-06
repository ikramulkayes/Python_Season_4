#Task 5 updated
def removeElm(lst,size,idx):

    if idx <0 or idx>=size:
        return "Get a valid index"
    while idx < size-1:
        
        lst[idx] = lst[idx+1]
        idx += 1
    lst[idx] = 0
    return lst

lst = [10,20,30,40,50,80,77]
print(removeElm(lst, 7,6))