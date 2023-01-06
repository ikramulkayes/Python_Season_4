def print_lefty(num):
    num = str(num)
    if num =="0":
        
        return ""
    else:
        k = print_lefty(int(num)-1)+num 
        print(k)
        return k
print_lefty(5)   
