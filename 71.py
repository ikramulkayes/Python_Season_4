def buble_sort(head,minval):  #for finding min val here minval is an object
    #print("gg")
    if head == None :
        return minval
    else:
        
        if head.elm <minval.elm:
            minval = head

        return buble_sort(head.next,minval)

def initerate(head,size): #for iteration
    temp = buble_sort(head,head)
    if size <= 0 or head==None :# for breaking
        return
    gg = head.elm  # this part is swapping
    head.elm = temp.elm
    temp.elm = gg
    size -= 1

    initerate(head.next, size)





class Node:  
    def __init__(self,val,next):
        self.elm = val
        self.next = next

lst = [55,42,6,1,3,4,0,-1]#this part creates linked list 
head = Node(lst[0],None)
obj = head

for elm in range(1,len(lst)):
    k = Node(lst[elm],None)
    obj.next = k
    obj = k

initerate(head, len(lst))

obj = head
while obj != None:
    print(obj.elm)
    obj = obj.next