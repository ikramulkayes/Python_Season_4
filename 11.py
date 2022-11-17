def leniar_to_circular(lst,start,size):
    last = size - 1
    first = 0
    for k in range(start):
        templ = lst[len(lst)-1]
        temp = lst[0]
        lst[0] = lst[-1]
        for elm in range(1,len(lst)):
            gg = temp
            temp = lst[elm]
            lst[elm] = gg
    return lst
linear=[10,20,30,40,50,0,0,0,0,0,0]
print(leniar_to_circular(linear, 8,5))

        

        


        
