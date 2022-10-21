class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, w in times:
            adj[s].append((w,d))
        
        # if len(adj[k]) == 0:
        #     print("error")
        #     return -1
        visited = set()
        
        minheap = [(0,k)]
        res = 0
        while minheap:
            cost, src = heapq.heappop(minheap)
            if src in visited:
                continue
            res = cost
            visited.add(src)
            for cst, dst in adj[src]:
                if dst not in visited:
                    heapq.heappush(minheap,((cost+cst), dst))
        
        if len(visited) == n:
            return res
        return -1