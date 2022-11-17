
#Task 6
def makeitvanish(lst,size,value):
    if size > len(lst):
        return "Take  the correct size"
    else:
        idx = 0
        while idx < size:
            if lst[idx] == value:
                i = idx
                while i < size:
                    lst[i] = lst[i+1]
                    i += 1
                lst[size-1] = 0
                size -= 1
            else:
                idx += 1
    return lst

source=[2,10,2,30,2,2,50,2,2,2,2,0,0]
print(makeitvanish(source,11,2))