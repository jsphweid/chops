"""
=== Brute Force Approach ===
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N = len(nums)
        total = 0
        for i in range(N):
            mi, ma = float("inf"), -float("inf")
            for j in range(i, N):
                mi = min(mi, nums[j])
                ma = max(ma, nums[j])
                total += ma - mi
        return total

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== Implemented Approach ===
I heard using a monotonic stack is good here...

The thing is monotonic stacks are help for finding next/prev lo/hi
and I'm not immediately sure how that is helpful here...

[1,2,3]
[2,3,N] next largest
[N,N,N] prev largest
[N,N,N] next smallest
[N,1,2] prev smallest

[2,6,5,1,3,7,4]
 2 6 5 1 3 7 4

Looked at hint 1:
Can you get the max/min of a certain subarray by using the max/min of a smaller subarray within it?

This makes me think of divide and conquer.
[2,6,5,1] min=1 max=6
[3,7,4] min=3 max=7
you can then find the min and max of the combined list by just min/maxing existing ones
min=1 max=7

But I'm not immediately sure how this translates into all possible combinations

Let's read hint 2.
Notice that the max of the subarray from index i to j 
is equal to max of (max of the subarray from index i to j-1) and nums[j].

Hmm... maybe monotonic can be viewed more than just "next" or "prev" largest.
[2,6,5,1,3,7,4] => 
[(2,2),(6,6),(5,6),(1,6),(3,6),(7,7),(4,7)]
so a tuple of the number and the largest we've seen up to that point
but wouldn't we want to do the the other way too?

[1,2,3]
largest from left, largest from right, smallest from left, smallest from right
[(1,1,3,1,1),(2,2,3,1,2),(3,3,3,1,3)]

I don't know...
Time to look at the discussions.

Reading Lee's briefly.
res = sum(A[i] * f(i)) 
    where f(i) is the number of subarrays, in which A[i] is the minimum.

Err... let's come back to this later...

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N = len(nums)
        total = 0
        for i in range(N):
            mi, ma = float("inf"), -float("inf")
            for j in range(i, N):
                mi = min(mi, nums[j])
                ma = max(ma, nums[j])
                total += ma - mi
        return total