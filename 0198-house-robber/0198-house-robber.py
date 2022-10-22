class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        cache = {0:nums[0]}
        for i in range(1,len(nums)):
            if i-2 < 0:
                take = nums[i] + 0
            else:
                take = nums[i] + cache[i-2]
            nottake = cache[i-1]
            cache[i] = max(take, nottake)
        return cache[len(nums)-1]
            
        ## Recursion Pick not-pick solution with Memoization Time O(N) Space O(N)+auxilary stackspace
        # def helper(i):
        #     if i == 0:
        #         return nums[0]
        #     if i <0:
        #         return 0
        #     if i in cache:
        #         return cache[i]
        #     cache[i] = max((nums[i] + helper(i-2)),(0 + helper(i-1)))
        #     return cache[i]
        # return helper(len(nums)-1)
        ## Recursion Pick not pick solution Time O(2^N) Space O(2^N)
        # def helper(i):
        #     if i == 0:
        #         return nums[0]
        #     if i < 0:
        #         return 0
        #     pick = nums[i] + helper(i-2)
        #     notpick = 0 + helper(i-1)
        #     return max(pick,notpick)
        # return helper(len(nums)-1)