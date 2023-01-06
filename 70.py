def buble_sort(head,count):  #    buble sort using linked list and recusion
    #print("gg")
    if head.next == None or count ==0: # breaking part 
        return 
    else:
        temp = head.next
        if head.elm > temp.elm: # this part swaps
            gg = head.elm
            head.elm = temp.elm
            temp.elm = gg

        buble_sort(head.next,count -1)

def initerate(head,size): #for iteration
    buble_sort(head,size)
    size -= 1
    if size <= 0: # breaking part 
        return
    initerate(head, size)




# this part creates linked list only 
class Node:
    def __init__(self,val,next):
        self.elm = val
        self.next = next

lst = [55,42,6,1,3,4,0]
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