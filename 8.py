def rightshift(lst,k):
    for elm in range(k):
        lindex = len(lst)-1
        i = 0
        temp = lst[lindex]
        while lindex > i:
            lst[lindex] = lst[lindex-1]
            lindex -= 1
        lst[0] =temp
    return lst
s = [10,20,30,40,50]
print(rightshift(s,3))
