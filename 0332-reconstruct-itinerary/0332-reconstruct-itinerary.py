class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        
        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i ,neigh in enumerate(temp):
                adj[src].pop(i)
                res.append(neigh)
                if dfs(neigh):
                    return True
                res.pop()
                adj[src].insert(i, neigh)
            return False
        
        dfs("JFK")
        return res