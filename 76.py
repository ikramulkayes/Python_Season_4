def func(lst,start=4,size=5,head=None):
    n = len(lst)
    last_index = (start + size-1)%n
    #print(last_index)
    
    if last_index <0:
        last_index = n -1
    m = lst[last_index]
    if m == None:
        return
    gg = Node(lst[last_index],None)
    head.next = gg
    head = gg
    start = start -1
    if start <0:
        start = n-1
    else:
        start = start % n
    func(lst,start,size,head)





class Node:  
    def __init__(self,val,next):
        self.elm = val
        self.next = next




lst = ["x","y",None,None,"a","b","c"]#this part creates linked list 
head = Node(None,None)
obj = head





#obj.next = head


obj = head
func(lst,4,5,obj)
obj = head
while obj != None:
    print(obj.elm)
    obj = obj.next
