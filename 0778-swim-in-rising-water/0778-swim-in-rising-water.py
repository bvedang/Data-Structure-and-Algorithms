class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        n = len(grid)
        visited = set()
        minheap = [(grid[0][0],0,0)]
        mincost = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while minheap:
            w1, si, sj = heapq.heappop(minheap)
            mincost = max(mincost,w1)
            if si == n-1 and sj == n-1:
                break
            if (si,sj) in visited:
                continue
            visited.add((si,sj))
            for dr,dc in directions:
                newsr = si + dr
                newdc = sj + dc
                if newsr < 0 or newsr == n or newdc < 0 or newdc == n or (newsr,newdc) in visited:
                    continue # we dont want to get index out of bound
                heapq.heappush(minheap,(max(w1,grid[newsr][newdc]), newsr, newdc))
                
        return mincost