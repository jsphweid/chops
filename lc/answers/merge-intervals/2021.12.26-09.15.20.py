"""
===== Initial Thoughts =====
seems like it involves search for an existing range.. so binary search might be reasonable
you can order them first. Actually just sort them and see if the next can go in the last

[1,3]
[1, 2]
l=0 r=1 m=0
l=1 r=1 m=1
2

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = []
        for start, end in intervals:
            if len(res):
                last_start, last_end = res[-1]
                if last_start <= start <= last_end:
                    res[-1] = [last_start, max(end, last_end)]
                    continue
            res.append([start, end])
        return res