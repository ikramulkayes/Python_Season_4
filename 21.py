#Task2
def rotateLeft(lst,k):
    
    for k in range(k):
        temp = lst[0]
        for elm in range(len(lst)-1):
            lst[elm] = lst[elm+1]
        lst[elm+1] = temp
    return lst

print(rotateLeft([10,20,30,40,50,60],11))