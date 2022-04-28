"""
===== Initial Thoughts =====
Spent a lot of time thinking of this but never arrived at the trick...

Looked up the answer though... Now I'm going to implement it myself.

~~Complexity Analysis
Time - O(n^2)
Space - O(n)

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        total = 0
        while len(arr) > 1:
            lowest = (float("inf"), 0, 0)
            for i, val in enumerate(arr):
                if i > 0:
                    lowest = min(lowest, (arr[i-1]*val, val, i))
                if i < len(arr) - 1:
                    lowest = min(lowest, (arr[i+1]*val, val, i))
            cost, _, i = lowest
            total += cost
            arr.pop(i)
        return total

"""

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        total = 0
        while len(arr) > 1:
            lowest = (float("inf"), 0, 0)
            for i, val in enumerate(arr):
                if i > 0:
                    lowest = min(lowest, (arr[i-1]*val, val, i))
                if i < len(arr) - 1:
                    lowest = min(lowest, (arr[i+1]*val, val, i))
            cost, _, i = lowest
            total += cost
            arr.pop(i)
        return total