"""
[1,2,3,4,6,8,10,11,5,-1] -> 7
  [1,1,1,2,2,2, 1,-6,-6]


1 2 3 4 5
1 2 3 4 5 6

=== Implemented Approach ===
do a diff array and then every time you get a new number
count forward that amount and then do maths to figure out how many it makes?
2(3) -> 1 (2 * 1/2)
3(4) -> 3 (3 * 2/2)
4(5) -> 6 (4 * 3/2)
5(6) -> 10 (5 * 4/2)

~~Complexity Analysis
Time - O(n)
Space - O(1)

FAILED on [1,2,3,8,9,10]
          [x,1,1,5,1,1]
"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return 0
        curr = nums[1] - nums[0]
        streak = 0
        total = 0

        def count(n):
            if n < 2: return 0
            return int(n * ((n - 1) / 2))

        for i in range(1, N):
            diff = nums[i] - nums[i - 1]
            if diff == curr:
                streak += 1
            else:
                total += count(streak)
                streak = 1
                curr = diff
        return total + count(streak)