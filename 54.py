class Node:
    def __init__(self,elm,next):
        self.elm = elm
        self.next = next

class profit_expert:
    def __init__(self):
        self.head = Node(None,None)
        self.obj = self.head
    def taking_array(self,lst,n=0):
        self.lst = lst
        gg =  self.profit(lst[n])
        self.obj.elm = gg
        tempnode = Node(None, None)
        self.obj.next = tempnode
        self.obj = tempnode
        #print(f"Investment: {lst[n]} Profit: {gg}")
        n += 1
        if n < len(lst):

            self.taking_array(lst,n)

        
            


    
    def profit(self,capital):
        if capital <= 25000:
            return 0.0
        elif capital <= 100000:
            return 45.0 + self.profit(capital-1000)
        elif capital > 100000:
            return 80.0 + self.profit(capital - 1000)
        else:
            return 0.0
    def print_profits(self):
        obj = self.head
        count = 0
        while obj.elm != None:
            print(f"Invesment: {self.lst[count]}; Profit: {obj.elm}")
            obj = obj.next
            count += 1


lst =[25000, 100000, 250000, 350000]       
s = profit_expert()
s.taking_array(lst)
s.print_profits()