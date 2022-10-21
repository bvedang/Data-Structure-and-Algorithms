class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def helper(i):
            if i < 2:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = min((cost[i-1] + helper(i-1)), cost[i-2] + helper(i-2))
            return cache[i]
        return helper(len(cost))
        