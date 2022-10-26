class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        if m == 1 and n == 1:
            return grid[0][0]
        cache = [[0]*n for i in range(m)]
        for r in range(m):
            if r == 0:
                cache[r][0] = grid[r][0]
            cache[r][0] = grid[r][0] + cache[r-1][0]
        for c in range(n):
            if c == 0:
                cache[0][c] = grid[0][c]
            cache[0][c] = grid[0][c] + cache[0][c-1]
        
        for r in range(1,m):
            for c in range(1,n):
                cache[r][c] = min(grid[r][c]+cache[r-1][c],grid[r][c]+cache[r][c-1])
        
        return cache[m-1][n-1]
#       Recursion Solution with memoization Time O(M*N) and space O(M*N) + On(m+n)
#         def helper(r,c):
#             if r<0 or c<0:
#                 return float("inf")
#             if r == 0 and c == 0:
#                 return grid[0][0]
#             if cache[r][c] != 0:
#                 return cache[r][c]
            
#             left = grid[r][c]+ helper(r-1,c)
#             top = grid[r][c] + helper(r,c-1)
#             cache[r][c] = min(left,top)
#             return cache[r][c]
#         return helper(len(grid)-1, len(grid[0])-1)
#        Recursion Solution Time O(2^M*N) and space O(2^M*N)
#         def helper(r,c):
#             if r<0 or c<0:
#                 return float("inf")
#             if r == 0 and c == 0:
#                 return grid[0][0]
            
#             left = grid[r][c]+ helper(r-1,c)
#             top = grid[r][c] + helper(r,c-1)
#             return min(left,top)
#         return helper(len(grid)-1, len(grid[0])-1)