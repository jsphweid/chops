"""
===== Initial Thoughts =====
0110 -> 1001 -> 0110 -> 1001
000010111 -> 100110100 -> 111010000 -> 001011001
23           308          464          89

=== Brute Force Approach ===
just rotate 3 times and see if those are any equal

[1,2,3]
[4,5,6]
[7,8,9]

[0,1]
[1,0]


"""

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        N = len(mat)
        def are_equal(one, two):
            for i in range(N):
                for j in range(N):
                    if one[i][j] != two[i][j]:
                        return False
            return True

        def rotate(matrix):
            res = []
            for col in zip(*matrix):
                res.append(list(reversed(list(col))))
            return res

        for _ in range(4):
            if are_equal(mat, target):
                return True
            mat = rotate(mat)
        return False