def groupSum(index,lst,num,lindex=1):
    print(index,lindex)
    if lindex+1 >= len(lst):
        index += 1
        if index >= len(lst):

            return False
        else:
            #print(lst[index] ,lst[lindex])
            lindex= index +1
            return groupSum(index, lst, num,lindex)
    
    elif (lst[lindex] +lst[lindex+1])==num -lst[index] or lst[lindex+1]==num -lst[index] or lst[lindex]==num -lst[index] :
        return True
    else:
        #print(lst[index] ,lst[lindex])
        lindex += 1
        return groupSum(index, lst, num,lindex)
    

print(    groupSum(0, [2, 4, 8], 9) )