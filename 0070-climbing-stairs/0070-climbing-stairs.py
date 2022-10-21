class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helper(n, cache):
            if n <=1:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = helper(n-1,cache) + helper(n-2, cache)
            return cache[n]
        return helper(n, cache)