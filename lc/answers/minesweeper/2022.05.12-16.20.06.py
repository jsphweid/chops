class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        M, N = len(board), len(board[0])
        click_i, click_j = click
        if board[click_i][click_j] == "M":
            board[click_i][click_j] = "X"
            return board

        def get_valid_neighbors(i, j):
            res = []
            for ii, jj in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]:
                if 0 <= i + ii < M and 0 <= j + jj < N:
                    res.append([i + ii, j + jj])
            return res

        def count_mines(i, j):
            total = 0
            for ii, jj in get_valid_neighbors(i, j):
                total += board[ii][jj] == "M"
            return total

        def reveal(i, j):
            if board[i][j] == "E":
                num_neighbor_mines = count_mines(i, j)
                if num_neighbor_mines > 0:
                    board[i][j] = str(num_neighbor_mines)
                else:
                    board[i][j] = "B"
                    for ii, jj in get_valid_neighbors(i, j):
                        reveal(ii, jj)

        reveal(click_i, click_j)
        return board