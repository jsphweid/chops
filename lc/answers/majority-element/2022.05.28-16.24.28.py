"""
===== Initial Thoughts =====
[1,1,1,2,2,2,2]
[2,2,2,2,1,1,1]

=== Brute Force Approach ===
if you could sort, then you could find the one with the longest streak
but that's not linear time

~~Complexity Analysis
Time - O(nlog(n)) Space - O(1)
or using more memory
Time - O(n) Space - O(n)

=== Implemented Approach ===
what's so special about 50%+ percent?

2 1 2 1 2

read some discussions

something about adding or subtracting 1
2 1 2 1 2
1 0 1 0 1 count

1 2 1 2 2
1 0 1 0 C (where C is change candidate, changes to 2)

1 1 2 2 2
1 2 1 C 1 (changes to 2)

2 2 2 1 1
1 2 3 2 1 (never changes from 2)

1 1 2 2 2 1 2
1 2 1 0 C 0 1

Similar to xor quesiton where we know all non answer will cancel just about everything else.

~~Complexity Analysis
Time - O(n)
Space - O(1)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate