class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0:1,1:1}
        if n < 2:
            return 1
        for i in range(2,n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]
        # def helper(n):
        #     if n < 2:
        #         return 1
        #     if n in cache:
        #         return cache[n]
        #     cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        #     return cache[n]
        # return helper(n)