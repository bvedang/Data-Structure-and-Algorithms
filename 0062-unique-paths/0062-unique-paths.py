class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for i in range(m)]
        def helper(r,c):
            if r < 0 or c < 0:
                return 0
            if r == 0 and c == 0 :
                return 1
            if dp[r][c] != 0:
                return dp[r][c]
            dp[r][c] = helper(r-1,c) + helper(r,c-1)
            return dp[r][c]
        return helper(m-1,n-1)