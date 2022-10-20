class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj =defaultdict(list)
        for s,d,w in times:
            adj[s].append((d,w))
        
        if k not in adj:
            return -1
        
        visited =set()
        minheap = [(0,k)]
        mincost = 1
        while minheap:
            w1, u1 = heapq.heappop(minheap)
            if u1 in visited:
                continue
            visited.add(u1)
            mincost = max(mincost,w1)
            for u2,w2 in adj[u1]:
                if u2 not in visited:
                    heapq.heappush(minheap,(w1+w2,u2))
        if len(visited) == n:
            return mincost
        return -1