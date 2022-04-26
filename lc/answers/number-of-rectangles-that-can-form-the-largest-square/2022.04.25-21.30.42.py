class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        best = count = 0
        for l, w in rectangles:
            val = min(l, w)
            if val > best:
                best = val
                count = 1
            elif val == best:
                count += 1
        return count
