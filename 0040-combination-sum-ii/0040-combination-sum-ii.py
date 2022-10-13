class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates.sort()
        def backtrack(i, comb):
            if sum(comb) == target:
                res.append(comb.copy())
                return
            if sum(comb) > target or i >= len(candidates):
                return 
            comb.append(candidates[i])
            backtrack(i+1, comb)
            comb.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1,comb)
        backtrack(0, comb)
        return res