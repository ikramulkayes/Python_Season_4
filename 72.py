def is_there_a_loop(head):
    temp = head  #this is stroring the starting head
    head = head.next #this is the head we going to itereate
    temp2 = temp  # this part will only iterate 
    flag = False
    limit = 1
    while head !=None:
        for i in range(limit):
            if temp2 == head:
                return True
            else:
                temp2 = temp2.next
        limit += 1
        temp2 = temp 
        head = head.next
    return False














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
#obj.next = head


obj = head
print(is_there_a_loop(head))