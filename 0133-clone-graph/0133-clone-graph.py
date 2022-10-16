"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        if len(node.neighbors) == 0:
            newNode = Node(node.val)
            return newNode
        
        oldtonew ={}
        oldtonew[node] = Node(node.val,[])
        q = deque()
        q.append(node)
        while q:
            for i in range(len(q)):
                n = q.popleft()
    
                for neighbor in n.neighbors:
                    if neighbor not in oldtonew:
                        oldtonew[neighbor] = Node(neighbor.val,[])
                        q.append(neighbor)
                    oldtonew[n].neighbors.append(oldtonew[neighbor])
        return oldtonew[node]
                
#         def dfs(node):
#             if node in oldtonew:
#                 return oldtonew[node]
#             copy = Node(node.val)
#             oldtonew[node] = copy
#             for neighbor in node.neighbors:
#                 copy.neighbors.append(dfs(neighbor))
#             return copy
        
#         return dfs(node)
                
                