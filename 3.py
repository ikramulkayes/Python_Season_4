#Task 8
def arraySeries(n):
    lst = [0]*(n*n)
    count = 0
    stepcount = n-1

    for i in range(1,n+1):
        for elm in range(i):
            lst[stepcount-elm] = elm+1
        stepcount+= n
    return lst

print(arraySeries(10))

        
            