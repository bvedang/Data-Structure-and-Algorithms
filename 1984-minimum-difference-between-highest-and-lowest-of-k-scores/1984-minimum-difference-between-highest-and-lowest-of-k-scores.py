class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums)-k+1):
            l,r = i,i+k-1
            print(nums[l],nums[r])
            min_diff = min(min_diff,nums[r]-nums[l])
                
        return min_diff
            