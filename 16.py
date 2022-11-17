def doubleRepeat(lst):
    rlst = []
    countlst = []
    flag = True
    for elm in lst:
        if len(rlst)==0:
            rlst.append(elm)
        else:
            for selm in rlst:
                if selm == elm:
                    flag = False
                    pass
            if flag == True:
                rlst.append(elm)
        if flag:
            count = 0
            for kelm in lst:
                if elm == kelm:
                    count+= 1
            
            countlst.append(count)
    checklst = [0]*len(lst)
    count = 0
    for elm in countlst:
        for selm in checklst:
            if elm >1 and elm==selm:
                return True
        checklst[count] = elm
        count+= 1
    return False

lst = [3,4,6,3,4,7,4,6,8,6,6,4,100,22]
print(doubleRepeat(lst))
        
    
                
            
