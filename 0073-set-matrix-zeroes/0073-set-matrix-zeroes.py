class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        locations = set()
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    locations.add((r,c))
                else:
                    continue
        def helper(mr,mc):
            for rin in range(row):
                matrix[rin][mc] = 0
            for cin in range(col):
                matrix[mr][cin] = 0
            return
        for r,c in locations:
            helper(r,c)
        
                    