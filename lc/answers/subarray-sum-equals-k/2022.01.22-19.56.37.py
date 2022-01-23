"""
===== Initial Thoughts =====
k=2 8
[-4,2,4,0,0,2,-2,5,5,2]
[-4,-2,2,2,2,4,2,7,12,14]
either something like DP or two pointer
the repetition is adding a similar series of numbers over and over again

really it's something like asking ourselves at some point how many times after
that does something have a certain sum.

=== Brute Force Approach ===
get every possible sublist and see if it sums to k

~~Complexity Analysis
Time - O(n^2)
Space - O(1) (really only have to store a count)

=== Implemented Approach ===
I'm reading answers now because it's been 30 minutes.

So i knew the duplication was in summing same numbers over and over, which points
to creating a running sum once. But I didn't know what to do with that.

[-4,2,4,0,0,2,-2,5,5,2]
[-4,-2,2,2,2,4,2,7,12,14] 1
counts={0:1,-4:1,-2:1}, res=0, curr=2

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts, res, running = {0:1}, 0, 0
        for num in nums:
            running += num
            # search for prev
            res += counts.get(running - k, 0)
            counts[running] = counts.get(running, 0) + 1
        return res
        