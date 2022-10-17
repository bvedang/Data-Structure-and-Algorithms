class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
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
            visited.remove(node)
            adj[node].clear()
            return True
        
        for i in range(numCourses):
            if not cycle(i, visited, path):
                return False
        return True
        
        