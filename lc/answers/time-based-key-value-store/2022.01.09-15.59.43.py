"""
=== Implemented Approach ===
dictionary with key mapping to a list of tuples
from the example
{
    foo: [(1, bar), (4, bar2)]
}

~~Complexity Analysis
Time - set O(1), get O(logn)

[1] 3
l=0 r=1 m=0
l=1
"""
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.store[key]
        if not lst: return ""
        l, r = 0, len(lst)
        while l < r:
            mid = (l + r) // 2
            time, val = lst[mid]
            if time == timestamp:
                return val
            if time < timestamp:
                l = mid + 1
            else:
                r = mid
        return "" if l == 0 else lst[l-1][1]





