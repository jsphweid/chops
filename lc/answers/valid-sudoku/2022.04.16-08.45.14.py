from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_cols = defaultdict(set)
        seen_squares = defaultdict(set)
        for i, row in enumerate(board):
            seen_row = set()
            for j, item in enumerate(row):
                if item != ".":
                    if item in seen_row: # check row
                        return False
                    seen_row.add(item)

                    if item in seen_cols[j]: # check col
                        return False
                    seen_cols[j].add(item)

                    square_key = (i//3, j//3)
                    if item in seen_squares[square_key]: # check square
                        return False
                    seen_squares[square_key].add(item)
        return True

