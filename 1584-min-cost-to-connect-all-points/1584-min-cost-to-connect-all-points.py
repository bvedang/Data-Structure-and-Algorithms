class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(len(points)):
            xi,yi = points[i]
            for j in range(i+1, len(points)):
                xj,yj = points[j]
                dist = abs(xi-xj) + abs(yi-yj)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        minheap = [(0,0)]
        visited = set()
        cost = 0
        while len(visited) < n:
            cst, src = heapq.heappop(minheap)
            if src in visited:
                continue
            cost += cst
            visited.add(src)
            for dist, sr in adj[src]:
                if sr in visited:
                    continue
                heapq.heappush(minheap, (dist, sr))
        
        return cost