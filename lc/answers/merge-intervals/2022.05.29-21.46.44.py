class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for l, r in intervals:
            if res and res[-1][0] <= l <= res[-1][1]:
                res[-1][1] = max(r, res[-1][1])
            else:
                res.append([l, r])
        return res
