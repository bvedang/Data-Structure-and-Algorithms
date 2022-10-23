class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]:
            return 0
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[0]*n for i in range(m)]
        def helper(r,c):
            if r<0 or c<0 or obstacleGrid[r][c] == 1:
                return 0
            if r == 0 and c ==0:
                return 1
            if dp[r][c] != 0:
                return dp[r][c]
            
            dp[r][c] = helper(r-1,c) + helper(r,c-1)
            return dp[r][c]
        return helper(len(obstacleGrid)-1,len(obstacleGrid[0])-1)
    
        ## Recursion Solution Time O(2^M*N) Space O(M) + O(M+N)
#          def helper(r,c):
#             if r<0 or c<0 or obstacleGrid[r][c] == 1:
#                 return 0
#             if r == 0 and c ==0:
#                 return 1
            
#             count = helper(r-1,c) + helper(r,c-1)
#             return count
#         return helper(len(obstacleGrid)-1,len(obstacleGrid[0])-1)