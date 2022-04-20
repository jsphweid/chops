class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = 1
        rr = intervals[0][1]
        for i in range(1, len(intervals)):
            r = intervals[i][1]
            if r > rr:
                rr = r
                res += 1
        return res
