class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        ops.append([m, n])
        left, right = float("inf"), float("inf")
        for op in ops:
            left = min(left, op[0])
            right = min(right, op[1])
        return left * right
