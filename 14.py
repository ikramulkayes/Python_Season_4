def insert_circular(lst,start,size,val,index):
    idx = index
    temp = lst[idx]
    idx += 1
    idx = idx%len(lst)
    for elm in range(1,size):
        gg = lst[idx]
        lst[idx] = temp
        temp = gg
        idx += 1
        idx = idx%len(lst)
    lst[index] = val
    return lst
lst = [0,0,1,2,3,4,5]
print(insert_circular(lst,2,5,100,4))


    