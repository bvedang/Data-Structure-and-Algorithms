class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        res = []
            
        def dfs(r,c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or i >= len(word) or board[r][c] != word[i] or (r,c) in visited:
                return False
            visited.add((r,c))
            res = (dfs(r+1,c, i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1, i+1))
            visited.remove((r,c))
            return res
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        for r in range(len(board)):
            for c in range(len(board[r])):
                if dfs(r,c,0):
                    return True
        return False