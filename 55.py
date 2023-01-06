class Node:
    def __init__(self,elm,next):
        self.elm = elm
        self.next = next

def sum_nodes(head):
    if head.next == None:
        return head.elm
    else:
        return head.elm + sum_nodes(head.next)

lst = [1,2,3,4,5,6]
head = Node(lst[0], None)
obj = head

for elm in range(1, len(lst)):
    temp = Node(lst[elm], None)
    obj.next = temp
    obj = temp

print(sum_nodes(head))


