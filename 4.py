#Task 9
def maxBunchcount(lst):
    maxcount = None
    count = None
    prev= None
    for elm in range(len(lst)):
        if prev == None and maxcount==None:
            prev = lst[elm]
            count = 1
            maxcount = 1
        elif lst[elm] == prev:
            #print(lst[elm])
            count += 1
            if count > maxcount:
                #print(lst[elm])
                #print(count)
                maxcount = count
        else:
            prev = lst[elm]
            count = 1
    return maxcount

lst = [1,1,1,1,1,1, 2, 2, 3,3,4, 4, 4, 4,3,3,3,3,3]
print(maxBunchcount(lst))

