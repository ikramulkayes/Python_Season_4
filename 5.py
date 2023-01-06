def repetition(lst):
    dic = {}
    for elm in lst:
        if elm not in dic.keys():
            dic[elm] = 1
        else:
            dic[elm] += 1
    lst = [0]*len(lst)
    count = 0
    for elm in dic.values():
        for k in lst:
            if elm >1 and elm == k:
                return True
        #print(count)
        lst[count] = elm
        count += 1
    return False


lst = [3,4,6,3,4,7,4,6,8,6,6]
print((repetition(lst)))
