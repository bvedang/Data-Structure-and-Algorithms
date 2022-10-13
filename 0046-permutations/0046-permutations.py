class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i == len(nums):
                return [[]]
            res = []
            per = helper(i+1)
            for p in per:
                for j in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(j, nums[i])
                    res.append(pcopy)
            return res
        
        return helper(0)