class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        sub = []
        def subsequence(i, sub):
            if i >= n:
                res.append(sub.copy())
                return
            sub.append(nums[i])
            subsequence(i+1, sub)
            sub.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            subsequence(i+1, sub)
        subsequence(0,sub)
        return res