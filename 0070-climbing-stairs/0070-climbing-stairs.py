class Solution:
    def climbStairs(self, n: int) -> int:
        #Top down Approcah with Space Optimization Time O(N) space O(1) 
        if n <2:
            return 1
        prev = prev2 = 1
        i = 2
        while(i <= n):
            curr = prev+prev2
            prev2 = prev
            prev = curr
            i += 1
        return prev
        #Top down Approcah Time O(N) space O(N) cache
        # if n <2:
        #     return 1
        # res = [1,1]
        # i = 2
        # while i <= n:
        #     res.append(res[i-1] + res[i-2])
        #     i +=1
        # return res[n]
        # Memoization Method  Time  O(N)  Space O(2*N) stack space, cache
        # cache = {}
        # def helper(n, cache):
        #     if n <=1:
        #         return 1
        #     if n in cache:
        #         return cache[n]
        #     cache[n] = helper(n-1,cache) + helper(n-2, cache)
        #     return cache[n]
        # return helper(n, cache)