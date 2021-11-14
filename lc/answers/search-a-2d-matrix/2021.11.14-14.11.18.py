# index 4 -> i=1,j=0 divmod(num, num_cols)

"""
[
    [1, 3, 5, 7],
    [10,11,16,20],
    [23,30,34,60]] 
l=0 r=11 m=5 divmod(5, 4)
l=0 r=5  m=2 divmod(2, 4)
l=0 r=2  m=1 divmod(1, 4)

[[4]] 4
l=0 r=0
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        l, r = 0, num_cols * num_rows - 1
        while l <= r:
            mid = (l + r) // 2
            i, j = divmod(mid, num_cols)
            num = matrix[i][j]
            if num == target: return True
            if l == r: break
            if num > target:
                r = mid
            else:
                l = mid + 1
        return False