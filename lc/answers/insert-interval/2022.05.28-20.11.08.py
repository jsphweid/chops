"""
===== Initial Thoughts =====
[[1,3],[2,5],[6,9]]
[2,5]

[[1,5],[6,9]]

res = [[1,2],[3,10]]
intervals = [[12,16]], newInterval = [4,8]

FAILED because I didn't consider what happens when intervals is empty
then failed because of some other stuff... this problem is tricky!

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        l, r = newInterval
        used = False
        for ll, rr in intervals:
            if ll <= l <= rr:
                res.append([ll, max(r, rr)])
                used = True
            elif res and res[-1][1] >= rr:
                continue
            elif res and res[-1][1] >= ll:
                res[-1][1] = rr
            else:
                res.append([ll, rr])
        if not used:
            res.append(newInterval)
            res.sort()
        return res


I think a better approach is just to add it and deal with everything after
intervals = [[1,2],[3,10],[12,16]]

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = intervals + [newInterval]
        intervals.sort()
        res = []
        for l, r in intervals:
            if res and res[-1][1] >= r:
                continue
            elif res and res[-1][1] >= l:
                res[-1][1] = r
            else:
                res.append([l, r])
        return res
