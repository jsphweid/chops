"""
===== Initial Thoughts =====
[1,2],[3,5],[6,7],[8,10],[12,16]
start_i=1, end_i=3
so for 4,8, find where 4 intersects, then 8... then do stuff

both are none
[[1,3],[6,9]]
[4,5]

start is not null
[[1,3],[6,9]]
[2,5]

end is not null
[[1,3],[6,9]]
[4,6]

[[0,10],[1,3],[6,9]]
[0,10]

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start_i, end_i, dels = None, None, set()
        for i, (start, end) in enumerate(intervals):
            if start <= newInterval[0] <= end:
                start_i = i
            if start <= newInterval[1] <= end:
                end_i = i
            if newInterval[0] < start and newInterval[1] > end:
                dels.add(i)

        if start_i != None and end_i != None:
            start = min(newInterval[0], intervals[start_i][0])
            end = max(newInterval[1], intervals[end_i][1])
            intervals[start_i: end_i + 1] = [[start, end]]
            return intervals
        elif start_i == None and end_i == None:
            if dels:
                tmp = []
                for i in range(len(intervals)):
                    if i not in dels:
                        tmp.append(intervals[i])
                intervals = tmp
            intervals.append(newInterval)
            intervals.sort(key=lambda interval: interval[0])
            return intervals
        elif start_i != None and end_i == None:
            start = intervals[start_i][0]
            end = max(newInterval[1], intervals[start_i][1])
            intervals[start_i] = [start, end]
        else:
            start = min(newInterval[0], intervals[end_i][0])
            end = intervals[end_i][1]
            intervals[end_i] = [start, end]

        if dels:
            tmp = []
            for i in range(len(intervals)):
                if i not in dels:
                    tmp.append(intervals[i])
            intervals = tmp

        return intervals



