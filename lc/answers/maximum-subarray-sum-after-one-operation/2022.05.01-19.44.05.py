"""
===== Initial Thoughts =====
how does max subarray work?
[-2,1,-3,4,-1,2,1,-5,4] => 6
[-2,-1,-4,0,-1,1,2,-3,1]

[5,4,-1,7,8]
[5,9]

[-2,-1]
[-2,-3]

[-1,-2]
[-1,-3]

So what can we do with exactly 1 squaring?
Well it makes numbers bigger (and positive).

  [2,-1,-4,-3] => 17
[0,2, 1,-3,-6]

  [1,-1,1,1,-1,-1,1] => 4
[0,1, 0,1,2, 1, 0,1]

if we square
  [1,-1,1,1,-1,-1,1]
[0,1, 2,3,4, 3, 2,3]

But we gotta square the right one...

=== Brute Force Approach ===
we could try each, this would be n^2

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== Implemented Approach ===
I wonder if we can know the location of the one we should square?
Or is there a way to try all of them in linear time?

Basically we change the narrative when we square something, a negative -4
becomes 16, a difference of 20.

  [2,3,-4,10]
[0,2,5, 1,11] -> 11 or 101 with squaring
10 -> 100 is a diff of 90, 90+11->101

  [10,-4,2,3]
[0,10, 6,8,11] -> 11 or 101 with squaring
10 -> 100 is a diff of 90, 90+11->101

  [10,-4,5,-2]
[0,10, 6,11,9] -> 11 or 101 with squaring

I'm tempted to find ideal subrange. Then square the number in there
that will have the most impact.

Or just find the biggest impact and add it to the total.
No that doesn't work

I can't do it!

Ahh, okay, 

[2,-1,-4,-3]
[2, 1, 16]
[4]

"""

class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        prev_sq = prev_normal = res = 0
        for num in nums:
            normal = max(num, prev_normal + num)
            sq = max(num**2, num**2 + prev_normal, num + prev_sq)
            res = max(res, sq)
            prev_sq, prev_normal = sq, normal
        return res










