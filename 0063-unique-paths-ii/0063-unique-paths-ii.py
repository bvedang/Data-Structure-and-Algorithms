class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]:
            return 0
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [0]*n
        for c in range(n):
            if obstacleGrid[0][c]:
                break
            dp[c] = 1
        
        for r in range(1,m):
            temp = [0]*n
            for c in range(0,n):
                if obstacleGrid[r][c] == 1:
                    continue
                if c == 0:
                    temp[c] = dp[c]
                else:
                    temp[c] = dp[c] + temp[c-1]
            dp = temp
        return dp[n-1]
         ## Top down approach Time O(M*N) space O(M*N)
#         for r in range(m):
#             if obstacleGrid[r][0] == 1:
#                 break
#             dp[r][0] = 1
            
#         for c in range(n):
#             if obstacleGrid[0][c] == 1:
#                 break
#             dp[0][c] = 1
#         for r in range(1,m):
#             for c in range(1, n):
#                 if obstacleGrid[r][c] == 1:
#                     continue
#                 dp[r][c] = dp[r-1][c] + dp[r][c-1]
#         print(dp)
#         return dp[m-1][n-1]
                
         ## Recursion Solution with Memoization Time O(M*N) Space O(M) + O(M+N)
#         def helper(r,c):
#             if r<0 or c<0 or obstacleGrid[r][c] == 1:
#                 return 0
#             if r == 0 and c ==0:
#                 return 1
#             if dp[r][c] != 0:
#                 return dp[r][c]
            
#             dp[r][c] = helper(r-1,c) + helper(r,c-1)
#             return dp[r][c]
#         return helper(len(obstacleGrid)-1,len(obstacleGrid[0])-1)
    
        ## Recursion Solution Time O(2^M*N) Space O(M) + O(M+N)
#          def helper(r,c):
#             if r<0 or c<0 or obstacleGrid[r][c] == 1:
#                 return 0
#             if r == 0 and c ==0:
#                 return 1
            
#             count = helper(r-1,c) + helper(r,c-1)
#             return count
#         return helper(len(obstacleGrid)-1,len(obstacleGrid[0])-1)