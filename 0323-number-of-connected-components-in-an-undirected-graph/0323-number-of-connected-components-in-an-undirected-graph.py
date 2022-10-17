class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {}
        rank ={}
        numcomp = [n]
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
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return
            if rank[n1] > rank[n2]:
                par[p2] = p1
                rank[p1] += 1
                numcomp[0] -=1
            elif rank[n1] < rank[n2]:
                par[p1] = p2
                rank[p2] += 1
                numcomp[0] -=1
            else:
                par[p2] = p1
                rank[p1] += 1
                numcomp[0] -=1
            return
        
        
        for edge in edges:
            union(edge[0],edge[1])
        
        return numcomp[0]