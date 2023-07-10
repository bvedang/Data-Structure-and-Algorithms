class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        def helper(mr,mc):
            for rin in range(row):
                if matrix[rin][mc] !=0:
                    matrix[rin][mc] = "0"
                else:
                    continue
            for cin in range(col):
                if matrix[mr][cin] != 0:
                    matrix[mr][cin] = "0"
                else:
                    continue
            return
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    helper(r,c)
                else:
                    continue
       
        for r in range(row):
            for c in range(col):
                if matrix[r][c]=="0":
                    matrix[r][c] = 0
        
                    