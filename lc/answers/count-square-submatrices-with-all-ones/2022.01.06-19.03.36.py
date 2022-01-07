"""
===== Initial Thoughts =====
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

[
    (0,1) (0,2) (0,3)
    (1,1) (1,2) (1,3)
    (2,1) (2,2) (2,3)
]

count largest squares and work inward?

rotation method?

7
1101 0011 1011
1001 1111 0110
1110 1100 0111

1,0,1
1,1,0
1,1,0

1,0,0
0,1,1
1,1,1

0,1,1
0,1,1
1,0,1

1,1,1
1,1,0
0,0,1

0110 1111 1110
1111 1111 1111
0111 1111 1011

0,1,1,1
1,1,1,1
0,1,1,1

1,1,1
1,1,1
1,1,1
0,1,0

1,1,1,0
1,1,1,1
1,1,1,0

0,1,0
1,1,1
1,1,1
1,1,1


1 0
0 0
0 1
1 1


=== Brute Force Approach ===
iterate through each one and count the squares it can add one

~~Complexity Analysis
Time - O(mn(m+n))
Space - O(m+n)


[ 3x3
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
(0,2)
ii, jj = 0, 2
horizontal=[] vertical=[]

my brute force works... 
then I read the discussions...


def get_lines(matrix, i, j, ii, jj):
    horizontal = matrix[ii][j:jj+1]
    vertical = []
    for x in range(len(horizontal) - 1):
        vertical.append(matrix[i + x][jj])
    return horizontal + vertical

def count_squares(matrix, i, j, M, N):
    count = 0
    ii, jj = i, j
    while ii != M and jj != N and all(get_lines(matrix, i, j, ii, jj)):
        count += 1
        ii += 1
        jj += 1
    return count

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        total, M, N = 0, len(matrix), len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                total += count_squares(matrix, i, j, M, N)
        return total

did the more optimal solution... but how does it make sense
[
  [0,1,1,1],
  [1,1,2,2],
  [0,1,2,3]
]
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        return sum(map(sum, matrix))
















