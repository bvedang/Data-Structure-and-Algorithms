class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        res = [0,1]
        i = 2
        while i <=n :
            res.append(res[i-1] + res[i-2])
            i += 1
        return res[n]