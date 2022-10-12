class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
            subsequence(i+1, sub)
        subsequence(0,sub)
        return res