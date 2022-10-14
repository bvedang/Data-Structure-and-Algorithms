class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return len([["Q"]])
        res =[0]
        cols = set()
        positive = set()
        negative = set()
        board = [["."]*n for i in range(n)]
        def helper(r):
            if r >= n:
                res[0] +=1
                return
            for c in range(n):
                if c in cols or (r+c) in positive or (r-c) in negative:
                    continue
                
                cols.add(c)
                positive.add(r+c)
                negative.add(r-c)
                board[r][c] = "Q"
                helper(r+1)
                cols.remove(c)
                positive.remove(r+c)
                negative.remove(r-c)
                board[r][c] = "."
        
        helper(0)
        return res[0]