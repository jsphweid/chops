"""
===== Initial Thoughts =====


=== Brute Force Approach ===
get all 3 combinations. check for triangle validity. keep the largest
O(n^3)

I think a better approach would be to sort
and to pick one and use two pointers to find the ideal 2/3?

1,6,3,4,7,8,3
sorted
1,3,3,4,6,7,8
clearly it's 6,7,8
1,3,8 nope
1,3,8 nope
1,4,8 13 - highest
1,6,8 15 - new highest
1,7,8 16 - new highest
3,3,8 14
3,4,8 15
3,6,8 17 - new highest
3,7,8 18 - new highest

etc.

~~Complexity Analysis
Time - O(n^2 + nlog(n))
Space - O(1)

i feel like this is kind of a waste though. Why not just sort and choose the three highest
if that doesn't make a valid triangle, then we need a good way to backoff. Could be a lot
faster.

6,7,8 is valid... but what if it's 6,7,14
3,4,6,7,14
4,6,7 is the next best thing. I guess we just shift everything over

=== Implemented Approach ===
sort then slide...

~~Complexity Analysis
Time - O(n) + O(nlogn)
Space - O(1)
"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if (nums[i + 1] + nums[i + 2]) > nums[i]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0
            
            