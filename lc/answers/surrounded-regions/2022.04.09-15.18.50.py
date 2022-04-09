
class Solution:
    def solve(self, A: List[List[str]]) -> None:
        M, N = len(A), len(A[0])

        def sink(i, j):
            if 0 <= i < M and 0 <= j < N and A[i][j] == "O":
                A[i][j] = "Z"
                for ii, jj in [(0,1),(1,0),(-1,0),(0,-1)]:
                    sink(ii + i, jj + j)


        for i, row in enumerate(A):
            for j, item in enumerate(row):
                if i == 0 or i+1 == M or j == 0 or j+1 == N:
                    sink(i, j)

        for i, row in enumerate(A):
            for j, item in enumerate(row):
                if item == "O":
                    A[i][j] = "X"
                elif item == "Z":
                    A[i][j] = "O"
        