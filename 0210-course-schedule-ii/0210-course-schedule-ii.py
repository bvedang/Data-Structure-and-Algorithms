class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        res =[]
        visited = set()
        path =set()
        def dfs(crs):
            if crs in path:
                return True
            if crs in visited:
                return False
            visited.add(crs) 
            for neighbor in premap[crs]:
                if dfs(neighbor) == False:
                    return False
            visited.remove(crs)
            path.add(crs)
            premap[crs] = []
            res.append(crs)
            return True
                
            
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res