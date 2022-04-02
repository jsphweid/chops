"""
===== Initial Thoughts =====
first initial thought is... isn't everything surrounded by X's
UNLESS it has at least 1 O on the edge?

Input
[["O","O","O","O","X","X"]
,["O","O","O","O","O","O"]
,["O","X","O","X","O","O"]
,["O","X","O","O","X","O"]
,["O","X","O","X","O","O"]
,["O","X","O","O","O","O"]]
Output
[
['T', 'T', 'T', 'T', 'X', 'X'], 
['T', 'T', 'T', 'T', 'T', 'T'], 
['T', 'X', 'T', 'X', 'T', 'T'], 
['T', 'X', 'T', 'O', 'X', 'T'], 
['T', 'X', 'T', 'X', 'T', 'T'], 
['T', 'X', 'T', 'T', 'T', 'T']]

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # iterate over the whole board
        # when you see an O, search all Os in group for an edge
        # if no edge O, then flip all of them
        # then continue... keep track of seen also

        def out_of_range(i, j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
                return True

        def outer_ring(i, j):
            if i == 0 or j == 0 or i + 1 == len(board) or j + 1 == len(board[0]):
                return True

        def flip_neighbor_o(i, j, char):
            board[i][j] = char
            for ii, jj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if not out_of_range(ii, jj) and board[ii][jj] == "O":
                    flip_neighbor_o(ii, jj, char)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and outer_ring(i, j):
                    flip_neighbor_o(i, j, "T")

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"