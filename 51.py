#insertion sort

def insertion_sort(lst):
    for i in range(1,len(lst)):
        j = i
        while j >0 and lst[j-1]>lst[j]:
            temp = lst[j]
            lst[j] = lst[j-1]
            lst[j-1] =temp
            j -= 1
    return lst


lst = [8,2,3,6,5,2]
print(insertion_sort(lst))