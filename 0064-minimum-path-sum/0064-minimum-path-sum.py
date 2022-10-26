class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        cache = [[0]*n for i in range(m)]
        
        def helper(r,c):
            if r<0 or c<0:
                return float("inf")
            if r == 0 and c == 0:
                return grid[0][0]
            if cache[r][c] != 0:
                return cache[r][c]
            
            left = grid[r][c]+ helper(r-1,c)
            top = grid[r][c] + helper(r,c-1)
            cache[r][c] = min(left,top)
            return cache[r][c]
        return helper(len(grid)-1, len(grid[0])-1)
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