class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        visited =set()
        walls = 0
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    q.append([r,c,0])
                    visited.add((r,c))
                if rooms[r][c] == -1:
                    walls +=1
        
        if len(q) == 0 or walls == (len(rooms) * len(rooms[0])):
            return rooms
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            for i in range(len(q)):
                r,c,steps = q.popleft() 
                for dr,dc in direction:
                    newdr, newdc = r+dr,c+dc
                    if newdr <0 or newdr == len(rooms) or newdc < 0 or newdc == len(rooms[0]) or rooms[newdr][newdc] != 2147483647 or (newdr,newdc) in visited:
                        continue
                    rooms[newdr][newdc] = 1 + min(rooms[newdr][newdc], steps)
                    visited.add((newdr,newdc))
                    q.append([newdr,newdc,steps+1])
        
        return rooms