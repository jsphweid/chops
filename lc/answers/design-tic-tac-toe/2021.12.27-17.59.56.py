"""
=== Implemented Approach ===
make a list that stores the state of the winning positions that get incremented when you 
add one to that row/col/diag

~~Complexity Analysis
Time - O(1)
Space - O(n)
"""

class TicTacToe:

    def __init__(self, n: int):
        size = 2 * n + 2
        self._state = {1: [0] * size, 2: [0] * size}
        self._n = n

    def move(self, row: int, col: int, player: int) -> int:
        n = self._n
        lst = self._state[player]
        lst[row] += 1
        lst[col + n] += 1
        if row == col: lst[-2] += 1
        if row + col + 1 == n: lst[-1] += 1

        return player if n in {lst[row], lst[col + n], lst[-2], lst[-1]} else 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)