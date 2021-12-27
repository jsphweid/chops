"""
XXX
000

0,0 [1,1,1,0,3,0,1,1] [1,1,1,3,0,0,1,1]
0,1
0,2
1,0
1,1
1,2
2,0
2,1
2,2
"""

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # each col is 0,1,2, row is 3,4,5 (left to right), diag is 6,7 (left, right)
        o_results, x_results = [0] * 8, [0] * 8
        num_o, num_x = 0, 0
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char != " ":
                    num_o += char == "O"
                    num_x += char == "X"
                    results = o_results if char == "O" else x_results
                    results[j] += 1
                    results[3 + i] += 1
                    if i == j:
                        results[6] += 1
                    if (i == 0 and j == 2) or (i == 2 and j == 0) or (i == 1 and j == 1):
                        results[7] += 1
        if num_o > num_x or num_x - num_o > 1:
            return False
        max_o, max_x = max(o_results), max(x_results)
        if max_o == 3 and max_x == 3:
            return False
        if max_x == 3 and num_x == num_o:
            return False
        if max_o == 3 and num_x != num_o:
            return False


        return True