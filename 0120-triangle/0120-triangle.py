class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[m-1])
        cache = [[0]*i for i in range(1,m+1)]
        
        for c in range(n):
            cache[m-1][c] = triangle[m-1][c]
        
        for r in range(m-2,-1,-1):
            for c in range(r,-1,-1):
                cache[r][c] = triangle[r][c] + min(cache[r+1][c], cache[r+1][c+1])
        
        return cache[0][0]
        
        
        
        
        ## Recursion with memoization Time(O(N*N) n = rows) Space O(N*N)+O(N)
#         def helper(r,c):
#             if r == m-1:
#                 return triangle[r][c]
            
#             if cache[r][c] != 0:
#                 return cache[r][c]
            
#             bottom = triangle[r][c] + helper(r+1,c)
#             right = triangle[r][c] + helper(r+1,c+1)
#             cache[r][c] =  min(bottom, right)
#             return cache[r][c]
#         return helper(0,0)