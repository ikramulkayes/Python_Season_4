def func(word,index=0,temp=""):
    a = word[index]
    flag = False
    for elm in temp:
        if elm == a:
            flag = True
    if flag:
        if index ==len(word)-1:
            return ""
        else:
            return func(word,index+1,temp)
    else:
        if index ==len(word)-1:
            return a
        elif a == " ":
            return a+ func(word,index+1)  
        else:
            temp += a
            return a+ func(word,index+1,temp)    

word = "programming is fun"
print(func(word))   