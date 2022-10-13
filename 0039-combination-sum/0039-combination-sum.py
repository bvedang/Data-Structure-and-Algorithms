class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def backtrack(i, comb):
            if sum(comb) == target:
                res.append(comb.copy())
                return
            if sum(comb) > target or i >= len(candidates):
                return
            
            comb.append(candidates[i])
            backtrack(i, comb)
            comb.pop()
            backtrack(i+1,comb)
        backtrack(0, comb)
        return res