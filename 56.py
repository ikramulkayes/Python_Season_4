def righttriangle(number, inc):
    suum = number+ inc
    if number <= 0:
        return 1
    else:
        blankspace(number - 1)
        increment(inc,number,suum)
        lefttriangle(number - 1, inc +1)
        
def blankspace(s_count):
    if s_count == 0:
        return
    else:
        print(" ", end = '')
        blankspace(s_count - 1)

    
def increment(count,number,suum):
    if count <= 0:
        return 
    else:
        increment(count - 1,number,suum)
        if count+number == suum:
            print(count)
        else:
            print(count, end = ' ')
            
righttriangle(5, 1)