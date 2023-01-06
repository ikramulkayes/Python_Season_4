def substring(word,index=0,flag=False):
    if index >= len(word):
        return 0 
    elif flag:
        if word[index] == "1":
            index += 1
            return 1 + substring(word,index, False)
        else:
            index += 1
            return substring(word,index, False)
    else:
        if word[index]  == "1":
            index += 1
            return substring(word,index, True)
        else:
            index += 1
            return substring(word,index, False)   

word = "111111a11"
print(substring((word)))