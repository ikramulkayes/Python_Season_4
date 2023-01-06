
    

def x_ditect(word):
    if len(word)>0:
        #print(word)
        gg = word[0]
        if gg == "x":
            return "x"+ x_ditect(word[1::])
        else:
            return x_ditect(word[1::])
    else:
        return ""
def not_x_ditect(word):
    if len(word)>0:
        #print(word)
        gg = word[0]
        if gg != "x":
            return  gg + not_x_ditect(word[1::])
        else:
            return not_x_ditect(word[1::])
    else:
        return ""    
def iterate(word):
    return x_ditect(word) + not_x_ditect(word)

word = "xxrivanxx"
print(iterate(word))