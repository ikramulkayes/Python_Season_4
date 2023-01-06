class wNode:
    def __init__(self,element,next,last):
        self.element = element
        self.next = next
        self.prev = last

class wLinkedlist:
    def __init__(self,lst):
        head = wNode(lst[0], None, None)
        tail = head
        for elm in range(1,len(lst)):
            elm = lst[elm]
            obj = wNode(elm, None, tail)
            tail.next = obj
            tail = obj
        head.prev = tail
        tail.next = head
        self.head = head
        self.tail = tail
        #print(tail.element)
    def printDoublycircular(self):
        print(self.head.element)
        obj = self.head.next
        while obj != self.head:
            print(obj.element)
            obj = obj.next

    def printDoublycircular_rev(self):
        print(self.tail.element)
        obj = self.tail.prev
        while obj != self.tail:
            print(obj.element)
            obj = obj.prev
    

    





    def func(self):
        print(self.head.element)
        Ttail = self.head
        obj = self.head.next
        sum1 = 0
        while obj.prev!= self.tail:
            sum1 += Ttail.element
            print(sum1)
            Ttail = obj
            obj = obj.next
        
        
lst = [10,20,100,200]
a1 = wLinkedlist(lst)
a1.printDoublycircular()
print("--------------")
a1.printDoublycircular_rev()
print("-------------------")
a1.func()