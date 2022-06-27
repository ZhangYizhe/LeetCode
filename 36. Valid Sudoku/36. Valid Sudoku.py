from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidRow(board) and self.isValidColumn(board) and self.isValidSquare(board)

    def isValidRow(self, board: List[List[str]]) -> bool:
        for row in board:
            temp_set = set()
            for point in row:
                if point == ".":
                    continue
                else:
                    if point not in temp_set:
                        temp_set.add(point)
                    else:
                        return False
        return True

    def isValidColumn(self, board: List[List[str]]) -> bool:
        for x in range(9):
            temp_set = set()
            for y in range(9):
                point = board[y][x]
                if point == ".":
                    continue
                else:
                    if point not in temp_set:
                        temp_set.add(point)
                    else:
                        return False
        return True

    def isValidSquare(self, board: List[List[str]]) -> bool:
        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                temp_set = set()
                for s_x in range(x, x + 3):
                    for s_y in range(y, y + 3):
                        point = board[s_x][s_y]
                        if point == ".":
                            continue
                        else:
                            if point not in temp_set:
                                temp_set.add(point)
                            else:
                                return False
        return True

board = [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

print(Solution().isValidSudoku(board))


