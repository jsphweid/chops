"""
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCB"

abce
sfcs
adee

["a","b"]
["c","d"]
acdb

dfs(0, 0, 0, {})
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        def dfs(i, j, word_i):
            if 0 <= i < M and 0 <= j < N:
                if word_i == len(word) - 1:
                    return word[word_i] == board[i][j]
                else:
                    if word[word_i] == board[i][j]:
                        board[i][j] = "#"
                        res = []
                        for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                            res.append(dfs(i+di, j+dj, word_i+1))
                        board[i][j] = word[word_i]
                        return any(res)
                    else:
                        return False
            else:
                return False
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if dfs(i, j, 0):
                    return True
        return False