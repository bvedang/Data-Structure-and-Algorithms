class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        for r in range(1,m):
            temp = [0]*n
            for c in range(0,n):
                if c == 0:
                    temp[c] = row[c]
                else:    
                    temp[c] = row[c] + temp[c-1]
            row = temp 
        return row[n-1]
        ## Top down Time O(M*N) space O(M*N)
#         dp = [[0]*n for i in range(m)]
#         for r in range(m):
#             dp[r][0] = 1
#         for c in range(n):
#             dp[0][c] =1
        
#         for r in range(1,m):
#             for c in range(1,n):
#                 dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
#         return dp[m-1][n-1]
        ## Recursion Solution with Memoization Time O(M*N) space O(M*N) +O((M-1)+(N-1))
#         dp = [[0]*n for i in range(m)]
#         def helper(r,c):
#             if r < 0 or c < 0:
#                 return 0
#             if r == 0 and c == 0 :
#                 return 1
#             if dp[r][c] != 0:
#                 return dp[r][c]
            
#             dp[r][c] = helper(r-1,c) + helper(r,c-1)
#             return dp[r][c]
#         return helper(m-1,n-1)
        ## Recursion Solution Time O(2^M*N) space O((M-1)+(N-1))
        # def helper(r,c):
        #     if r < 0 or c < 0:
        #         return 0
        #     if r == 0 and c == 0 :
        #         return 1
        #     count = helper(r-1,c) + helper(r,c-1)
        #     return count
        # return helper(m-1,n-1)