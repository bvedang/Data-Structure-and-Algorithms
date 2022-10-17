class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par ={}
        rank ={}
        def find(n):
            if n not in par:
                par[n] = n
                rank[n] = 0
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            
            else:
                par[p1] = p2
                rank[p1] += 1
            return True
        
        if len(edges) != n-1:
            return False
        
        for e1,e2 in edges:
            if not union(e1,e2):
                print(e1,e2)
                return False
        return True