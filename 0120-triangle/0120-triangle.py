class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[m-1])
        cache = [0]*m
        
        for c in range(n):
            cache[c] = triangle[m-1][c]
        
        for r in range(m-2,-1,-1):
            temp = [0]*(r+1)
            for c in range(r,-1,-1):
                
                temp[c] = triangle[r][c] + min(cache[c], cache[c+1])
            print(cache)
            cache = temp
        return cache[0]
        
        
        
        
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