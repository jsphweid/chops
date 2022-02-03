"""
===== Initial Thoughts =====
2
1 2
1 2

1 2
2 1

1 2 3
1 2 3
3 2 1
1 3 2
2 3 1
2 1 3
3 1 2
3 2 1 

doodled this on the board

=== Brute Force Approach ===
solve it like a graph and figure out all paths and add them

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

count(2, [1,2,4]) -> 2
    count(3, [2,4]) -> 0
    count(3, [1,4]) -> 1
        count(4, [4]) -> 1
            count(5, []) -> 1
    count(3, [1,2]) -> 1
        count(4, [2]) -> 1
            count(5, []) -> 1

class Solution:
    def countArrangement(self, n: int, nums=None) -> int:
        if n < 4: return n
        def count(n, nums):
            if not nums:
                return 1
            res = 0
            for i, x in enumerate(nums):
                if n % x == 0 or x % n == 0:
                    res += count(n + 1, nums[:i] + nums[i+1:])
            return res
        return count(1, list(range(1, n + 1)))


So I went up by default but after reading the discussions... going down is far better
because the lower numbers match with just about everything. You can weed out paths
in the DFS faster by going downward.

count(4, [1,2,3,4])
"""

class Solution:
    def countArrangement(self, n: int, nums=None) -> int:
        if n < 4: return n
        def count(n, nums):
            if not nums:
                return 1
            res = 0
            for i, x in enumerate(nums):
                if n % x == 0 or x % n == 0:
                    res += count(n - 1, nums[:i] + nums[i+1:])
            return res
        return count(n, list(range(1, n + 1)))


