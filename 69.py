def func(word,val,n,low=0,high=None):
    if high == None:
        high = len(val)
    if n >0:
        if high > len(word):
            return False
        temp = word[low:high]
        if temp == val:
            n -= 1
            low += len(val)
            high += len(val)
        else:
            low += 1
            high += 1
        return func(word, val, n,low,high)
    else:
        return True


word = "catcowcat"
print(func(word, "cow", 1))