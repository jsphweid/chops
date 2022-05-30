"""
===== Initial Thoughts =====
just use binary search

input = 7
2 4 5 8 10
T T T F F
0 1 2 3 4
      3 4
    2

input = 4
2 3 4
T T T

FAILED ON basic example...

{
    foo: [(1, bar)]
}

I didn't think through the nuances of BS at the edges
"""

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.map[key] and self.map[key][-1][1] == value:
            # if there is already something there and last val is
            # the same as this one, then just update last val
            self.map[key].pop()

        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.map[key]
        N = len(lst)
        l, r = 0, N - 1
        if N == 0:
            return ""
        while l < r:
            mid = (l + r) // 2
            mid_time, val = lst[mid]
            if mid_time == timestamp:
                return val
            if mid_time < timestamp:
                l = mid + 1
            else:
                r = mid

        if l == 0: 
            return "" if lst[l][0] > timestamp else lst[l][1]
        if l == N - 1 and lst[l][0] <= timestamp:
            return lst[l][1]
        return lst[l - 1][1]

"""
["TimeMap","set","set","get","get","get","get","get"]
[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
set love high 10
set love low 20
get love 5
get love 10
get love 15
get love 20
get love 25

(10, high), (20, low)
"""
