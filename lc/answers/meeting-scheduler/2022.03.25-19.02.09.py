"""
===== Initial Thoughts =====
did this problem with Brian

slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
[60,68]

starts = [0,10,60,60,140]
ends = [15,50,70,120,210]
[(0,1), (10, 1), (15, -1), (50, -1), (60, 1), (60, 1), (70, -1), (120, -1), (140, 1), (210, -1)]
0 1
10 2
15 1
50 0
60 1
60 2
70 1
120 0
140 1
210 0

Got the idea to do this from a book.
class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        lst = []
        for start, end in slots1 + slots2:
          lst.append((start, 1))
          lst.append((end, -1))
        lst.sort()
        overlap = 0
        for i, (time, inc) in enumerate(lst):
          overlap += inc
          if overlap == 2:
            if lst[i + 1][0] - time >= duration:
              return [time, time + duration]
        return []

my initial solution was the above, but Brian and I talked about how to make it
better afterwards and I had a few ideas which I'll implement now...

[[0,1000000000]]
[[0,1000000000]]
1000000
[0,0]
[1000000000, 1000000000]
[(0, 1), (0, 1), (1000000000, -1), (1000000000, -1)]
"""

class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        lst = []
        for start, end in slots1 + slots2:
          lst.append((start, 1))
          lst.append((end, -1))
        lst.sort()
        overlap = 0
        for i, (time, inc) in enumerate(lst):
          overlap += inc
          if overlap == 2:
            if lst[i + 1][0] - time >= duration:
              return [time, time + duration]
        return []
