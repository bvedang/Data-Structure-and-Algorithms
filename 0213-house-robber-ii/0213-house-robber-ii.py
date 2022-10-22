class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=3:
            return max(nums)
        
        def helper(num):
            prev = num[0]
            prev2 = 0
            for i in range(1,len(num)):
                curr = max((num[i] + prev2), prev )
                prev2 = prev
                prev = curr
            return prev
        exfirst = nums[1:]
        exlast = nums[:len(nums)-1]
        ans1 = helper(exfirst)
        ans2 = helper(exlast)
        return max(ans1, ans2)
    
        
            
            