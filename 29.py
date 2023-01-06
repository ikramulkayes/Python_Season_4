def sorting_with_plusminus(lst,size):
    for i in range(size):
        for j in range(size-i-1):
            if lst[j] <0 and lst[j+1]>=0:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    print(lst)


def finding_range(lst,size,num):
    for i in range(size):
        sum1 = 0
        for j in range(i,size):
            sum1 += lst[j]
            if sum1 == num:
                print((i+1),(j+1))
                return
    print("NO NO")
def finding_largest_sequence(lst,size):
    for i in range(size):
        for j in range(size-i-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    maxcount = None
    count = 0
    #print(lst)
    for i in range(size-1):
        num1 = lst[i]
        num2 = lst[i+1]
        if num2 - num1 ==1:
            count += 1
            if maxcount == None:
                maxcount = count
            elif count > maxcount:
                maxcount = count
            
        else:
            count = 0
    print(maxcount+1)
def rotateleft(lst,k):
    for i in range(k):
        temp = lst[0]
        for j in range(len(lst)-1):
            lst[j] = lst[j+1]
        lst[j+1] = temp
    print(lst)













#arr = [1, -1, 3, 2, -7, -5, 11, 6,None,None]
#sorting_with_plusminus(arr, 8)
lst = [1,9,3,10,4,20,2]
#finding_range(lst, 10, 15)
#finding_largest_sequence(lst, 7)
rotateleft(lst, 10)
