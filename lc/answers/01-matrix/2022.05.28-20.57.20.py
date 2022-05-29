"""
===== Initial Thoughts =====
I think it's just the minimum of the 4 directions + whatever it currently is
no that can't be it
why not just have a function that does BFS looking nearest 0 and then cache

from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        new_mat = [row[:] for row in mat]
        
        @cache
        def find_nearest(i, j):
            queue = deque([[i, j]])
            seen = set()
            distance = -1
            while queue:
                distance += 1
                for _ in range(len(queue)):
                    ii, jj = queue.popleft()
                    if mat[ii][jj] == 0:
                        return distance
                    for change_i, change_j in [[1,0],[0,1],[-1,0],[0,-1]]:
                        nxt_i = ii + change_i
                        nxt_j = jj + change_j
                        if 0 <= nxt_i < M and 0 <= nxt_j < N and (nxt_i, nxt_j) not in seen:
                            seen.add((nxt_i, nxt_j))
                            queue.append([nxt_i, nxt_j])

        for i in range(M):
            for j in range(N):
                if mat[i][j] == 1:
                    new_mat[i][j] = find_nearest(i, j)
        return new_mat

but times out as expected, even with cache...
really we need to cache better than this...

I tried doing DFS but it was getting too weird.

I need a new approach.

How about this. Just change all 1's to None's. And note the 0's.

Then take all the 0's and change all the surrounding None's to 1's and note the 1's.
Then take all the 1's and change all the surrounding None's to 2's and note the 2's.
etc.

"""
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        queue = deque([])
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = None
        curr = 0
        while queue:
            curr += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for ii, jj in [[1,0],[0,1],[-1,0],[0,-1]]:
                    ii = i + ii
                    jj = j + jj
                    if 0 <= ii < M and 0 <= jj < N and mat[ii][jj] is None:
                        mat[ii][jj] = curr
                        queue.append((ii, jj))
        return mat