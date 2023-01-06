class Node:   #linked list
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
    def palindrome_check(self):
        gg = self.countlen()
        lcount = gg-1
        fcount = 0
        flag = True
        for i in range(gg//2):
            obj = self.head
            count = 0
            fnum = 0
            lnum = 0
            while obj != None:
                if count == fcount:
                    fnum = obj.elem
                if count == lcount:
                    lnum = obj.elem
                count += 1
                obj = obj.next
            lcount -= 1
            fcount +=1
            if fnum != lnum:
                flag = False
                break
        print(flag)
    def phd_friend(self):
        result = Node(None, None)
        times = int(input())
        for i in range(times):
            pass
    def swap_start_last(self,k):
        count = 0
        obj = self.head
        while obj != None:
            count += 1
            obj = obj.next
        obj1 = self.head
        for i in range(count//2):
            obj2 = self.head

            for m in range(count-i-1): #check it out 
                obj2 = obj2.next
            
            if i == k:
                temp = obj1.elem
                obj1.elem = obj2.elem
                obj2.elem = temp
                #print("YO")
                break
            obj1 = obj1.next
    def is_there_a_loop2(self):
        temphead = Node(None, None)
        flag = True
        obj = self.head
        count = 0
        while obj != None:
            temptail = temphead  #none none
            temptail2 = None
            while temptail != None:
                if temptail.elem == obj:
                    flag = False
                    break
                temptail2 = temptail
                temptail = temptail.next
            if count == 0:
                temphead.elem = obj
                count += 1
            else:
                gg = Node(obj, None)
                temptail2.next = gg
            if flag == False:
                break
            obj = obj.next
        if flag:
            print("NO loop")
        else:
            print("There is loop")



            













        
                

                    





lst1 = [1,2,3,2,1]
lst2 = [1,2,3,4,5]
s = LinkedList(lst1)
o = LinkedList(lst2)
#s.rightshift()
#s.similar(o)
#o.even_at_first()
#o.printforward()
#s.palindrome_check()
o.swap_start_last(1)
o.printforward()
o.is_there_a_loop2()


        

