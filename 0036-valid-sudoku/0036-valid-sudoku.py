class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        matrix = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in matrix[(r//3,c//3)]:
                    return False
                else:
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    matrix[(r//3,c//3)].add(board[r][c])
        return True