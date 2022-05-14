class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = set(range(left, right + 1))
        for l, r in ranges:
            nums -= set(range(l, r + 1))
        return len(nums) == 0