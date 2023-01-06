class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

lst = [10,20,30,40]
obj = Node(lst[0], None)
head = obj
for elm in range(1,len(lst)):
    k = Node(lst[elm], None)
    obj.next = k
    obj = k

def reverse_print(head):
    if head.next == None:
        print(head.val)
    else:
        reverse_print(head.next)
        print(head.val)


reverse_print(head)
