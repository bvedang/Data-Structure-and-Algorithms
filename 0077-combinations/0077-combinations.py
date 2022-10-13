class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        res =[]
        def backtrack(i, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            if i > n:
                return 
            comb.append(i)
            backtrack(i+1, comb)
            comb.pop()
            backtrack(i+1, comb)
        backtrack(1,comb)
        return res