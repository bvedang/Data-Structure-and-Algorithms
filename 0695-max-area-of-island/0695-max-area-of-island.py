class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited =set()
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols  or (r,c) in visited or grid[r][c] ==0 :
                return 0
            visited.add((r,c))
            return 1+dfs(r,c+1)+dfs(r,c-1)+dfs(r+1,c)+dfs(r-1,c)
            
            
            
        for r in range(rows):
            for c in range(cols):
                    maxArea = max(maxArea,dfs(r,c))
                    
                    
        return maxArea