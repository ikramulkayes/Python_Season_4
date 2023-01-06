def reverse(lst):
    lastidx = len(lst)
    i = 0
    while i < lastidx:
        temp = lst[i]
        lst[i] = lst[lastidx-1]
        lst[lastidx-1] = temp
        lastidx-= 1
        i += 1
        #print(lst)
    return lst

lst = [1,2,3,4,5,6,7]
print(reverse(lst))
        

    