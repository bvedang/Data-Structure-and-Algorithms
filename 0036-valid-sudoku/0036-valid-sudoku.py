class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        matDict = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowDict[r] or board[r][c] in colDict[c] or board[r][c] in matDict[(r//3,c//3)]:
                    return False
                rowDict[r].add(board[r][c])
                colDict[c].add(board[r][c])
                matDict[(r//3,c//3)].add(board[r][c])
        return True