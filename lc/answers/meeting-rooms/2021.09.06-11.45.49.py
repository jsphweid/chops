"""
we could order them all in ascending order by the first index in each sub-array.
Then we can assert that the first index of an item must be greater than the second index of the previous item.

[[0,30],[5,10],[15,20]]
5 is less than 30, so it can't work out

Presumably if they have the same number, that's kosher?

[[2,4], [7,10]]
7 is greater than 4, so that's good.

"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] < sorted_intervals[i - 1][1]:
                return False
        return True
        