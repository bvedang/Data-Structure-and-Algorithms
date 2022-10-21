class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) <= 2:
            return min(cost[1], cost[0])
        step1 = step2 = 0
        i = 2
        while i <= len(cost):
            currcost = min((cost[i-1] + step1), (cost[i-2] + step2))
            step2 = step1
            step1 = currcost
            i += 1
        return step1
        
        
        # Top bottom Time complexity O(N) space O(N)
        # if len(cost) <= 2:
        #     return min(cost[1], cost[0])
        # cache={0:0, 1: 0}
        # i = 2
        # while i <= len(cost):
        #     cache[i] = min((cost[i-1] + cache[i-1]), (cost[i-2] + cache[i-2]))
        #     i += 1
        # return cache[len(cost)]
                
        
        # Memoization Time complexity O(N) space O(N*2)
        # cache = {}
        # def helper(i):
        #     if i < 2:
        #         return 0
        #     if i in cache:
        #         return cache[i]
        #     cache[i] = min((cost[i-1] + helper(i-1)), cost[i-2] + helper(i-2))
        #     return cache[i]
        # return helper(len(cost))
        