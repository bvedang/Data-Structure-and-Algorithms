class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if len(grid) == 1:
            return grid[0][0]
        
        minheap = [(grid[0][0],0, 0)]
        time = 0
        visited = set()
        direction = [(1,0), (-1,0), (0,1),(0,-1)]
        while minheap:
            cost, r,c = heapq.heappop(minheap)
            time = max(cost,time)
            if r == n-1 and c == n-1:
                return time
            if (r,c) in visited:
                continue
            visited.add((r,c))
            
            for dr, dc in direction:
                newrow = dr + r
                newcol = dc + c
                if newrow < 0 or newrow == n or newcol < 0  or newcol == n or (newrow,newcol) in visited:
                    continue
                heapq.heappush(minheap, (max(cost, grid[newrow][newcol]), newrow,newcol))
                