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
            # comb.append(i)
            # backtrack(i+1, comb)
            # comb.pop()
            # backtrack(i+1, comb)
            for j in range(i, n+1):
                comb.append(j)
                backtrack(j+1, comb)
                comb.pop()
        backtrack(1,comb)
        return res