class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## Topological sort
        adj ={}
        for i in range(numCourses):
            if i not in adj:
                adj[i] = []    
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited = set()
        
        
        def cycle(node,visited, path):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if not cycle(neighbor, visited, path):
                    return False
                adj[node].pop(adj[node].index(neighbor))
            visited.remove(node)
            return True
        
        for i in range(numCourses):
            if not cycle(i, visited, path):
                return False
        return True
        
        