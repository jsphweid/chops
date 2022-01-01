
def zero_row(matrix, i):
    for j in range(len(matrix[0])):
        matrix[i][j] = 0

def zero_col(matrix, j):
    for i in range(len(matrix)):
        matrix[i][j] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])
        zeros, rows_zeroed, cols_zeroed = [], set(), set()
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == 0:
                    zeros.append((i, j))
        for i, j in zeros:
            if i not in rows_zeroed:
                zero_row(matrix, i)
                rows_zeroed.add(i)
            if j not in cols_zeroed:
                zero_col(matrix, j)
                cols_zeroed.add(j)
