def least_diff(lst,start,end,size):  #circular
    flst = []
    min = None
    for i in range(size):
        temp = (start+i+1)%len(lst)
        #print(temp)

        m = lst[(start+i)%len(lst)]
        #print(m)
        #print("YO")
        while temp != (end+1)%len(lst):

            #print(temp)
            #print(min)
            #print(temp)
            k = lst[temp]
            if k == None:
                break
            if m >= k:
                sum1 = m - k
            else:
                sum1 = k - m
            if min == None:
                min = sum1
            elif sum1 < min:
                min = sum1
            temp = (temp+1)%len(lst)
    print(min)

def sum_of_diff(lst,start,end,size):
    sum1 = 0
    for i in range(size):
        elm1 = lst[(start+i)%len(lst)]
        elm2 = lst[(start+i+1)%len(lst)]
        print(elm1,elm2)
        if elm2 == None:
            break
        if elm1 >= elm2:
            sum1 += elm1 - elm2
        else:
            sum1 += elm2 - elm1
    if lst[start] > lst[end]:
        sum1 += lst[start] - lst[end]
    else:
        sum1 += -lst[start] + lst[end]
    print(sum1)

def ninja_thing(lst,start,end,size):
    flst = [None]*size
    for i in range(size):
        flag = True
        elm = lst[(start+i)%len(lst)]
        for j in range(size):
            j = (j+start+i) % len(lst)
            temp = lst[j]
            if temp != None:
                if temp > elm:
                    flst[i] = temp
                    flag = False
                    break
        if flag:
            flst[i] = -1
    print(flst)
def resizing(lst,start,end,size,newsize):
    newlst = [None]*newsize
    oldidx = start
    newidx = start
    for i in range(size):
        oldidx = (start+i)%len(lst)
        newidx = (start+i)%len(newlst)
        newlst[newidx] = lst[oldidx]
    print(newlst)

def insert(lst,start,end,size,idx,val): #check this out
    temp = lst[(idx+start)%len(lst)]
    lst[(idx+start)%len(lst)] = val

    for i in range(idx+1, size+1):
        k = lst[(i+start)%len(lst)]
        lst[(i+start)%len(lst)] = temp
        temp = k
    print(lst)
def last_prime(lst,size):
    count = 0
    idx = 0
    for i in range(size):
        elm = lst[i]
        if elm == 1:
            continue
        flag = True
        for j in range(2,elm):
            if elm %j ==0:
                flag = False
                break
        if flag == True:
            idx = i
            count += 1
    newlst = [None]*count
    start = count - 1
    newcount = start
    for i in range(size):
        elm = lst[(idx+i)%(size)]
        if elm == 1:
            continue
        flag = True
        for j in range(2,elm):
            if elm %j ==0:
                flag = False
                break
        if flag == True:
            newlst[newcount] = elm
            newcount -= 1
    print(newlst)




        



        








lst = [7,1,11,5,4,8,31,9,6,None,None]
#least_diff(lst, 3, 0, 4)
#sum_of_diff(lst, 3, 0, 4)
#ninja_thing(lst, 3, 0, 4)
#resizing(lst, 3, 0, 4, 4)
print(lst)
#insert(lst, 3, 0, 4, 4, 99)
last_prime(lst, 9)
        
