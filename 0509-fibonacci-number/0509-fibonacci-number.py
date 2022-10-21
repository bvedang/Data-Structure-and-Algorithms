class Solution:
    def fib(self, n: int) -> int:
        if n <2:
            return n
        
        zero, one = 0,1
        
        i = 2
        while i <= n:
            temp = one
            one = zero+one
            zero = temp
            i +=1 
        return one