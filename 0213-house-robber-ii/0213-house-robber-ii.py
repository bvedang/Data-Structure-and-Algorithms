class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        def helper(num):
            prev = num[0]
            prev2 = 0
            for i in range(1,len(num)):
                curr = max((num[i] + prev2), prev )
                prev2 = prev
                prev = curr
            return prev
    
        return max(helper(nums[1:]), helper(nums[:-1]))
    
        
            
            