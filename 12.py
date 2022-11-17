def leniar_to_circular(lst,start,size):
    final = [0]*len(lst)
    i = 0
    index = start

    while i < size:
        final[index] = lst[i]
        index += 1
        i += 1
        index = index%len(lst)
    return final

linear=[10,20,30,40,50,0,0,0,0,0,0]
print(leniar_to_circular(linear, 8,5))