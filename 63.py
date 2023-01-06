def countPairs(word,prevprevelm=None,prevelm=None,index=0):
    if index >= len(word):
        return 0
    elif prevelm == None:
        prevelm = word[index]
        index += 1
        return countPairs(word,None,prevelm,index)
    elif prevprevelm==None:
        prevprevelm = prevelm
        prevelm = word[index]
        index += 1
        return countPairs(word,prevprevelm,prevelm,index)
    elif word[index] == prevprevelm:
        prevprevelm = prevelm
        prevelm = word[index]
        index += 1
        return 1 + countPairs(word,prevprevelm,prevelm,index)
    else:
        prevprevelm = prevelm
        prevelm = word[index]
        index += 1
        return  countPairs(word,prevprevelm,prevelm,index)    

word = "axa"
print(countPairs(word))    
        