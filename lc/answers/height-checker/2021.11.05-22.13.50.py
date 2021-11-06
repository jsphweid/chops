class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(map(lambda t: t[0] != t[1], zip(heights, sorted(heights))))

