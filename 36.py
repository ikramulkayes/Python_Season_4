times = int(input())
lst = []
for elm in range(times):
    k = int(input())
    l = (input())
    l = l.split(" ")
    lst.append(l)

result = []
for elm in lst:
    sum1 = 0
    templst = []
    for selm in elm:
        
        selm = int(selm)
        if selm in templst or (-selm) in templst:
            if selm in templst:
                templst.remove(selm)
            else:
                templst.remove(-selm)
            templst.append(selm)
        else:
            templst.append(selm)
            
    result.append(sum(templst))
#print(result)
count = 1
for elm in result:
    print(f"Case {count}: {elm}")
    count += 1




