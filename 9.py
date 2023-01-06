def forwardprintcirculararray(lst,start,size):
    index = start
    i = 0
    while i < size:
        print(lst[index])
        index += 1
        index = index% len(lst)
        i += 1
s = [40,50,0,0,0,0,0,0,10,20,30]
print(forwardprintcirculararray(s,8,5))