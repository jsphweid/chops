"""
===== Initial Thoughts =====
so clearly the negative numbers are the hard thing about this problem
[-1,-2,-3] => -6
but if it were: [-1,-2,-3,-4] it'd probably still be -6 since we have to choose 3 negatives (all nums are negative)
and -6 is greater than -24. It's as if we want high numbers but if we're forced into negatives, we want low numbers.

=== Brute Force Approach ===
brute force would be to get all combinations of 3 numbers, multiply it -> then get the max of that arr

how can we do better?

what if we sorted
[-5, -4, -3, 1,2,3,4] -> -4, -5, 4 => 80 how do we know to grab 5,4 though
we can always try the lowest two with the highest num, i.e. index 0, 1, -1, then -1, -2, -3 and choose the max
when does that not work though?
-4, -3, -2, -1, 0 -> max is 0 works
-4, -3, -2, -1, 1 -> max is 12, works
-4, -3, 1, 2 -> max is 24

I think this may just work...

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===
get max between the last 3 indices and last 1 plus first two

~~Complexity Analysis
Time - O(nlogn)
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])