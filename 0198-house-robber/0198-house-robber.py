class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {}
        def helper(i):
            if i == 0:
                return nums[0]
            if i <0:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max((nums[i] + helper(i-2)),(0 + helper(i-1)))
            return cache[i]
        return helper(len(nums)-1)
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