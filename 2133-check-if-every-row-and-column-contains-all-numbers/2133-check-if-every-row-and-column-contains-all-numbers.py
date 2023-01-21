class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rows = defaultdict(set)
        cols = defaultdict(set)
        for row in range(n):
            for col in range(n):
                rows[row].add(matrix[row][col])
                cols[col].add(matrix[row][col])                
        
        for row in rows.keys():
            if len(rows[row]) < n:
                return False
        for col in cols.keys():
            if len(cols[col]) < n:
                return False
        
        return True