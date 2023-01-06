def inserting(s,index,value,size):
    if size > len(s):
        return "Fix your size"
    elif index <0 or index > size:
        return "Fix your index"
    count = size
    while count > index:
        s[count] = s[count-1]
        count -= 1
    s[index] = value
    return s


s = [10,20,30,40,50,0,0,0]

print(inserting(s, 0,200,5) )