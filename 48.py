def print_righty(num,count=0):
    num = str(num)
    
    if num =="0":
        
        return ""
    else:
        count += 1
        k = print_righty(int(num)-1,count)+num 
        print(" "*(count-1)+str(k))
        return k
print_righty(5)   
