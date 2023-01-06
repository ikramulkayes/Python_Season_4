def hocBuilder(height): 
    if height ==0:
        return 0
    elif height ==1:
        return 8
    else:
        return 5 + hocBuilder(height-1)

print(hocBuilder(3))