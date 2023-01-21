class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows= defaultdict(set)
        cols = defaultdict(set)
        n = len(matrix)
        for r in range(n):
            for c in range(n):
                if matrix[r][c] in rows[r] or matrix[r][c] in cols[c]:
                    return False
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
                
        return True