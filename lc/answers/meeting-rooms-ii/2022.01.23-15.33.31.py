"""
===== Initial Thoughts =====
[[0,30],[5,10],[15,20]]
0                   30
   5 10  15 20

0 start
5 start
10 end
15 start
20 end
30 end

(()())

0-5
1-2
4-6
6-8
7-9
7-10

0 start
1 start
2 end
4 start
5 end
6 end
6 start
7 start
7 start
8 end
9 end
10 end

(()())((()))

(0,'e')

=== Implemented Approach ===
seems pretty easy. We'll just change everything to a list of tuples (num, 'start' | 'end')
then sort by nums
then do a stack pushing an item on if it is 'start', and popping an item off if it is 'end'.
The max length of the stack is the answer.

May not matter but ends should come first to keep the stack the smallest... and 'end' < 'start' so sort
will be good.

~~Complexity Analysis
Time - O(n + nlogn)
Space - O(n)

tracing
[[0,30],[5,10],[15,20]]
0, 'start'
5, 'start'
10, 'end'
15, 'start'
20, 'end'
30, 'end'

Looking at lee215's answer... it is more clever to use -1 and 1 instead of 'start'/'end'
because not only do they sort the same (-1 == end, which comes before 1 == start), but you
can conveniently use those nums instead of later doing: `1 if s == "start" else -1`
but I'll leave mine since it's not too bad
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        lst, curr, res = [], 0, 0
        for start, end in intervals:
            lst.append((start, 'start'))
            lst.append((end, 'end'))
        lst.sort()
        for _, s in lst:
            curr += 1 if s == "start" else -1
            res = max(res, curr)
        return res