class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)-1
        res =[]
        for index, val in enumerate(nums):
            if index > 0 and val == nums[index-1]:
                continue
            l = index+1
            r = n
            while l < r:
                total = val + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([val, nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        
        return res