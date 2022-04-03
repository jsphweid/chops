class Solution:
    def solve(self, board: List[List[str]]) -> None:
        M, N = len(board), len(board[0])

        def flip_o(i, j, char):
            if board[i][j] == "O":
                board[i][j] = char
                for ii, jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0 < ii < M and 0 < jj < N:
                        flip_o(ii, jj, char)

        for i in range(M):
            flip_o(i, 0, "Y")
            flip_o(i, N - 1, "Y")
        for j in range(N):
            flip_o(0, j, "Y")
            flip_o(M - 1, j, "Y")

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == "Y":
                    board[i][j] = "O"
                elif char == "O":
                    board[i][j] = "X"




