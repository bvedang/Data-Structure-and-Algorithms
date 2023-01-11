class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            if i == 1:
                res[i] = prefix
                prefix = nums[i]
                continue
            res[i] = res[i-1] * prefix 
            prefix = nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*postfix
            postfix *= nums[i]
        
        return res