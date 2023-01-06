n = 8
lst = [None]*(n+1) 
lst[0] = 0
lst[1] = 1
def fibonachi(n,lst):
    if lst[n] != None:
        return lst[n]
    else:
        gg = fibonachi(n-1,lst) + fibonachi(n-2,lst)
        lst[n] = gg
        return gg 

print(fibonachi(n,lst))

