class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        atl = set()
        paci = set()
        
        def dfs(r,c, prevheight, visit):
            if ((r,c) in visit or r < 0 or r == rows or c < 0 or c == cols or heights[r][c] < prevheight):
                return
            visit.add((r,c))
            dfs(r+1,c, heights[r][c],visit)
            dfs(r-1,c, heights[r][c],visit)
            dfs(r,c+1, heights[r][c],visit)
            dfs(r,c-1, heights[r][c],visit)
            
        
        for c in range(cols):
            dfs(0,c, heights[0][c], paci)
            dfs(rows-1, c, heights[rows-1][c], atl)
        
        for r in range(rows):
            dfs(r,0, heights[r][0], paci)
            dfs(r, cols-1, heights[r][cols-1], atl)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in paci:
                    res.append([r,c])
        return res