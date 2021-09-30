"""
===== Initial Thoughts =====
This problem is annoying because it isn't specific about the inclusive/exclusive nature of the connections

=== Brute Force Approach ===
for each range, look at all the other ranges and see if either start or end is included in current range

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== Implemented Approach ===
order it first by the start time. then compare end of one to beginning of previous.
if there is "overlap" then return False
if ya reach the end, it's True

~~Complexity Analysis
Time - O(2nlogn)
Space - O(n) - if you used sorted instead of sort
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2: return True
        sorted_intervals = sorted(intervals, key=lambda i: i[0])
        for i in range(1, len(sorted_intervals)):
            curr = sorted_intervals[i]
            prev = sorted_intervals[i - 1]
            if curr[0] < prev[1]:
                return False
        return True