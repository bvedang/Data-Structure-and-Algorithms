class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:    
        time, fresh = 0,0
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                ## getting count of fresh oranges
                if grid[row][col] == 1:
                    fresh +=1
                ## getting locatin of all rotten oranges
                if grid[row][col] == 2:
                    q.append([row,col])
        
        neighbour = [(0,1),(0,-1),(1,0),(-1,0)]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                
                for dr, dc in neighbour:
                    newdr , newdc = r+dr,c+dc
                    if (newdr <0 or newdc <0  or newdr == len(grid) or newdc == len(grid[0]) or grid[newdr][newdc] != 1):
                        continue
                    grid[newdr][newdc] = 2
                    q.append([newdr,newdc])
                    fresh -= 1
            time += 1
        
        if fresh == 0:
            return time
        return -1
        
        