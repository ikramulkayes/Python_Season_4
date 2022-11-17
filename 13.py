def resizing_circular(lst,start,size):
    final = [0]*size
    index1 = start
    index2 = start
    i = 0
    while i < len(lst):
        final[index2] = lst[index1]
        index1 += 1
        index2 += 1
        index1 = index1 % len(lst)
        index2 = index2% len(final)
        i += 1
    return final
circ=[20,30,40,50,10]
print(resizing_circular(circ,4,7))
