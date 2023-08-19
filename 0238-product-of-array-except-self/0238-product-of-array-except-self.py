class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        post = 1
        pre =1
        for i in range(len(nums)):
            res.append(pre)
            pre = pre*nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            res[i] = post*res[i]
            post = post*nums[i]
        
        return res
        