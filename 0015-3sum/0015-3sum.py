class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        
        for idx, val in enumerate(nums):
            if idx >0 and val == nums[idx-1]:
                continue
            l,r = idx+1, len(nums)-1
            while l < r:
                total = nums[l] + val + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res