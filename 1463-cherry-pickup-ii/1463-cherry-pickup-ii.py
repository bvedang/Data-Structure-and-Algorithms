class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0]*n for _ in range(n)] for __ in range(m)]

        for row in reversed(range(m)):
            for col1 in range(n):
                for col2 in range(n):
                    result = 0
                    # current cell
                    result += grid[row][col1]
                    if col1 != col2:
                        result += grid[row][col2]
                    # transition
                    if row != m-1:
                        result += max(dp[row+1][new_col1][new_col2]
                                      for new_col1 in [col1, col1+1, col1-1]
                                      for new_col2 in [col2, col2+1, col2-1]
                                      if 0 <= new_col1 < n and 0 <= new_col2 < n)
                    dp[row][col1][col2] = result
        return dp[0][0][n-1]
        
#         m = len(grid)
#         n = len(grid[0])
#         cache = [[[0 for i in range(n)] for i in range(n)] for i in range(m) ]
        
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     cache[m-1][i][j] = grid[m-1][i]
#                 else:
#                     cache[m-1][i][j] = grid[m-1][i]+ grid[m-1][j]
#         print(cache)
        
#         for i in range(m-2,-1,-1):
#             for j in range(n):
#                 for k in range(n):
#                     maxi = 0
#                     direction = [-1,0,1]
#                     for l in direction:
#                         for o in direction:
#                             val = 0
#                             if j == k:
#                                 val = grid[i][j]
#                             else:
#                                 val = grid[i][j]+grid[i][k]
#                             if(j+l >= 0 and j+l < n and k+o >=0 and k+o <n):
#                                 val += cache[i+1][j+l][k+o]
#                             else:
#                                 val += float("-inf")
#                             maxi = max(maxi,val)
#                     cache[i][j][k] = maxi
        
#         return cache[0][0][n-1]
                    
        
#         Memoization
#         def helper(r,c1,c2):
#             if c1<0 or c1>= n or c2<0 or c2>=n:
#                 return float("-inf")
#             if r == m-1:
#                 if c1 == c2:
#                     return grid[r][c1]
#                 else:
#                     return grid[r][c1]+grid[r][c2]
#             if cache[r][c1][c2] != 0:
#                 return cache[r][c1][c2]
                
#             maxi = 0
#             direction = [-1,0,1]
            
#             for i in direction:
#                 for j in direction:
#                     if c1 == c2:
#                         maxi = max(maxi, grid[r][c1] + helper(r+1,c1+i,c2+j))
#                     else:
#                         maxi = max(maxi, grid[r][c1]+grid[r][c2] + helper(r+1,c1+i,c2+j))
#             cache[r][c1][c2] = maxi
#             return cache[r][c1][c2]
        
#         return helper(0,0,n-1)
#     Recursion
#         def helper(r,c1,c2):
#             if c1<0 or c1>= n or c2<0 or c2>=n:
#                 return float("-inf")
#             if r == m-1:
#                 if c1 == c2:
#                     return grid[r][c1]
#                 else:
#                     return grid[r][c1]+grid[r][c2]
#             maxi = 0
#             direction = [-1,0,1]
            
#             for i in direction:
#                 for j in direction:
#                     if c1 == c2:
#                         maxi = max(maxi, grid[r][c1] + helper(r+1,c1+i,c2+j))
#                     else:
#                         maxi = max(maxi, grid[r][c1]+grid[r][c2] + helper(r+1,c1+i,c2+j))
#             return maxi
        
#         return helper(0,0,n-1)