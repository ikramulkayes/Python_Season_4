
#Task 6 updated
def makeitvanish(lst,size,value):

    idx = 0
    while idx < size:
        if lst[idx] == value:
            i = idx
            while i < size-1:
                lst[i] = lst[i+1]
                i += 1
            lst[i] = 0
            lst[size-1] = 0
            size -= 1
        else:
            idx += 1
    return lst

source=[2,2,10,2,30,2,2,50,2,2,2,2,5]
print(makeitvanish(source,13,2))