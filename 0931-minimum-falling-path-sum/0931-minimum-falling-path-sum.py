class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        cache = [[0]*n for i in range(n)]
        for c in range(n):
            cache[0][c] = matrix[0][c]
        for r in range(1,n):
            for c in range(n):
                if c == 0:
                    cache[r][c] = matrix[r][c] + min(cache[r-1][c], cache[r-1][c+1])
                elif c == n-1:
                    cache[r][c] = matrix[r][c] + min(cache[r-1][c], cache[r-1][c-1])
                else:
                    cache[r][c] = matrix[r][c] + min(cache[r-1][c], cache[r-1][c-1],cache[r-1][c+1])
        res = float("inf")
        for c in range(n):
            res = min(res, cache[n-1][c])
        return res
        
#         Recursion with Memoizatin Time(O(N^2)) Space O(N^2) + O(N)
#         def helper(r,c):
#             if c<0 or c >= n:
#                 return float("inf")
#             if r == n-1 and c < n:
#                 return matrix[r][c]
#             if cache[r][c] !=0:
#                 return cache[r][c]
#             # down = matrix[r][c] + helper(r+1,c)
#             # left = matrix[r][c] + helper(r+1,c-1)
#             # right = matrix[r][c] + helper(r+1,c+1)
#             cache[r][c] = matrix[r][c] + min(helper(r+1,c),helper(r+1,c-1),helper(r+1,c+1))
#             return cache[r][c]
#         res = helper(0,0)
#         for i in range(1,n):
#             res = min(res, helper(0,i))
        
#         return res
#         Recursion Solution Time O(3^N) space(3N)
#         def helper(r,c):
#             if c<0 or c >= n:
#                 return float("inf")
#             if r == n-1:
#                 return matrix[r][c]
            
#             # down = matrix[r][c] + helper(r+1,c)
#             # left = matrix[r][c] + helper(r+1,c-1)
#             # right = matrix[r][c] + helper(r+1,c+1)
#             return matrix[r][c] + min(helper(r+1,c),helper(r+1,c-1),helper(r+1,c+1))
#         res = helper(0,0)
#         for i in range(1,n):
#             res = min(res, helper(0,i))
        
#         return res