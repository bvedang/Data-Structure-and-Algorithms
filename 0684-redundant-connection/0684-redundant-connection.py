class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}
        
        def find(n):
            if n not in par:
                par[n] = n
                rank[n] =0
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            if rank[n1] > rank[n2]:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] +=1
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        