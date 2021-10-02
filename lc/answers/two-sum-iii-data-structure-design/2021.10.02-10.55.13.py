"""
===== Initial Thoughts =====
should be easy if we solve like the original two sum problem -- keeping a set of all values.
Each time find is called with a num, we scan the set once, introspectively looking for the compliment.

This is O(n) lookup time.

=== Brute Force Approach ===
add numbers to a list. When find is called, do two loop technique... this is pretty expensive though and there
is no reason to do it. It shouldn't save memory because you still have to store the numbers. The set method
listed above is way better computationally and has roughly the same space (list vs. set)

~~Complexity Analysis
Time - O(n^2)
Space - O(n)

=== Implemented Approach ===
Keep a set of all nums described above.

~~Complexity Analysis
Time - add O(1), find O(n)
Space - O(n)

forgot keeping counts is important here...
space is like O(2n) now
"""
from collections import defaultdict
class TwoSum:

    def __init__(self):
        self._counts = defaultdict(int)

    def add(self, number: int) -> None:
        self._counts[number] += 1

    def find(self, value: int) -> bool:
        nums = self._counts.keys()
        for num in nums:
            compliment = value - num
            if num == compliment and self._counts[num] < 2:
                continue
            if compliment in nums:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)