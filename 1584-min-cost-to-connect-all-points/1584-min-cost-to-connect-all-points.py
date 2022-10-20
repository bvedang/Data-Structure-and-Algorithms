class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        visited = set()
        minheap = [(0,0)]
        cost = 0
        while len(visited) < len(points):
            c,i = heapq.heappop(minheap)
            if i in visited:
                continue
            cost += c
            visited.add(i)
            for dist, j in adj[i]:
                if j not in visited:
                    heapq.heappush(minheap, (dist,j))
        
        return cost