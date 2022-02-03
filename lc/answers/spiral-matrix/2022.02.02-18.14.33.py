def rotate(m):
    return list(zip(*m))[::-1]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lol = []
        while matrix:
            lol.append(matrix.pop(0))
            matrix = rotate(matrix)
        res = []
        for row in lol:
            for item in row:
                res.append(item)
        return res