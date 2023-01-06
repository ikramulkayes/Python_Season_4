class FinalQ:
    def print(self,lst,n=0):
        
        gg =  self.profit(lst[n])
        print(f"{n+1}.Investment: {lst[n]} Profit: {gg}")
        n += 1
        if n <= (len(lst)-1):
            self.print(lst,n) 


        
            


    
    def profit(self,capital):
        if capital <= 25000:
            return 0.0
        elif capital <= 100000:
            return 45.0 + self.profit(capital-1000)
        elif capital > 100000:
            return 80.0 + self.profit(capital - 1000)
        else: 
            return 0.0



lst =[25000, 100000, 250000, 350000]       
s = FinalQ()
s.print(lst,0)