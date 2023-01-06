class Node:
    def __init__(self,val,next):
        self.elm = val
        self.next = next

def isloop(head):
    obj = head
    temphead = Node(None, None)
    flag = True
    while obj!= None:
        tempobj = temphead
        tempprev = None
        while tempobj != None:
            #print("YO")
            if tempobj.elem == obj:
                print("YO")
                flag = False
                break
            tempprev = tempobj
            tempobj =   tempobj.next
        kk = Node(obj,None)
        tempprev.next = kk
        tempprev = kk
        if flag == False:
            
            break
        obj = obj.next
    if flag:
        print("False")
    else:
        print("True")


class Node:   #circular linked list
    def __init__(self, elem, next): 
        self.elem = elem
        self.next = next

class LinkedList:
    def __init__(self,lst):
        self.head = Node(lst[0],None)
        tail = self.head

        for elm in range(1,len(lst)):
            obj = Node(lst[elm], None)
            tail.next = obj
            
            tail = obj
        tail.next = self.head
        
            
    def printforward(self):
        obj = self.head
        while obj != None:
            print(str(obj.elem)+", ",end="")
            obj = obj.next

    def rightshift(self):
        obj = self.head
        obj1 = self.head.next
        temp = obj.elem
        while obj1 != None:
            k = obj1.elem
            obj1.elem = temp
            temp = k
            obj1 = obj1.next
        self.head.elem = temp
    def similar(self,other):
        obj1 = self.head
        
        fobj = None
        tail = None
        fhead = None

        while obj1 != None:
            #print("YO")
            obj2 = other.head
            x = obj1.elem
            while obj2 != None:
                #print(x,obj2.elem)
                if x == obj2.elem:
                    #print("YO")
                    if fobj == None:
                        fobj = Node(x, None)
                        tail = fobj
                        fhead = fobj
                    else:
                        fobj = Node(x, None)
                        tail.next = fobj
                        tail = fobj
                obj2 = obj2.next
            obj1 = obj1.next
        
        obj = fhead
        while obj != None:
            print(str(obj.elem)+", ",end="")
            obj = obj.next
    def countlen(self):
        count = 0
        obj = self.head
        while obj != None:
            count += 1
            obj = obj.next
        return count
    def even_at_first(self):
        obj = self.head
        count = self.countlen()
        for i in range(count):
            obj1 = obj
            obj2 = obj1.next
            for j in range(count-i-1):
                if obj1.elem%2 !=0 and obj2.elem%2 ==0:
                    temp = obj1.elem
                    obj1.elem = obj2.elem
                    obj2.elem = temp
                obj1 = obj1.next
                obj2 = obj2.next
                if obj2 == None:
                    print("_______")
                    break
    def is_there_a_loop(self):
        tail = self.head
        obj = self.head.next
        tempobj = Node(tail, None)
        temphead = tempobj
        flag = True
        while obj!= None:
            #print(obj.elem)
            tempobj = temphead
            while tempobj.next != None:

                if tempobj.elem == obj:
                    flag = False
                    break
                tempobj = tempobj.next
            tail = obj
            obj = obj.next
            k = Node(tail, None)
            tempobj.next = k
            tempobj = k
            if flag == False:
                break
        if flag:
            print("False")
        else:
            print("True")
    def is_there_a_loop2(self):
        temphead = Node(None, None)
        flag = True
        obj = self.head
        count = 0
        while obj != None:
            temptail = temphead
            temptail2 = None
            while temptail != None:
                if temptail.elem == obj:
                    flag = False
                    break
                
                temptail2 = temptail
                temptail = temptail.next
            if flag == False:
                break
            else:
                if count == 0:
                    temphead.elem = obj
                    count += 1
                else:
                    #print(count)
                    gg = Node(obj, None)
                    temptail2.next = gg

                obj = obj.next
        if flag:
            print("NO loop")
        else:
            print("There is loop")




        
                

                    





lst1 = [1,2,3,4,5]
lst2 = [17,15,8,12,10,5,4,1,7,6]
s = LinkedList(lst1)
o = LinkedList(lst2)
#s.rightshift()
#s.similar(o)
#o.even_at_first()
#o.printforward()
o.is_there_a_loop2()


        



isloop(o.head)

        



            



    