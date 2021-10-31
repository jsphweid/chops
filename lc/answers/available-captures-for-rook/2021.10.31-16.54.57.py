"""
===== Initial Thoughts =====
let's solve this making a bunch of small fn's
"""

def get_rook_rows(board):
    # given a board, return the two lists comprising the horizontal/vertical squares a rook occupies
    for i, row in enumerate(board):
        try:
            j = row.index("R")
            column = []
            for _row in board:
                column.append(_row[j])
            return row, column
        except:
            pass
    # should always find one...


def count_pawns_on_rook_row(rook_row):
    # assuming we have a rook, count pawns it can attack... maximum 2
    left = False
    right = False
    rook_has_been_found = False
    for piece in rook_row:
        if piece == "R": 
            rook_has_been_found = True
        else:
            if rook_has_been_found:
                # must be after the rook
                if piece == "B":
                    break  # don't worry about resetting right to False because if it was True, it happened before and that's ok
                elif piece == "p":
                    right = True
            else:
                # must be before the rook
                if piece == "B":
                    left = False
                elif piece == "p":
                    left = True
    return left + right


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        one, two = get_rook_rows(board)
        return count_pawns_on_rook_row(one) + count_pawns_on_rook_row(two)
        