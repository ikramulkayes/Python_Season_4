def selection_sort(lst):  #selection sort
    for i in range(len(lst)):
        minnum_idx = i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[minnum_idx]:
                minnum_idx = j
        if minnum_idx != i:
            temp = lst[i]
            lst[i] = lst[minnum_idx]
            lst[minnum_idx] = temp
    return lst

lst = [1,5,6,7,2,3]
print(selection_sort(lst))