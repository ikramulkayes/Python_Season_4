class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 7 and n > 0:
            
            return True
        else:
            lst = []

            n = abs(n)
            for elm in range(7,n):
                print("YO")
                if elm == (n//2) +1:
                    break
                if n%elm ==0:
                    
                    lst.append(elm)
               

            if len(lst)>0:
                return False
            else:
                return True

s = Solution()
print(s.isUgly(-2147483648))