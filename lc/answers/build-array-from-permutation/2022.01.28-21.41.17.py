"""

original solution 

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]


I thought long and hard how to do this in O(1) memory but just couldn't.
The best I could do was an O(n^2) time solution but that's not good enough.
Titles on the discussion indicate it can be done in O(n).

Looking up answers now...

Wow. Interesting solution I read about. Something I didn't consider was this problem essentially
comes down to storing two numbers in one number if you want O(1) time. When I was trying to think
of a way, I was thinking about how I could do it based on order. That clearly doesn't work, but this does.

A number can be broken into quotient / remainder with the help of some other numbers

nums = [5,0,1,2,3,4]

so in this example, at index 0, we want to replace the value with 4, but we also want to store 5
How do we store both? Well 5 can be represented as 5%6, 11%6, 17%6, etc. So how do we represent
the 4? 5%6=0, 11%6=1, 17%6=2, 23%6=3, 29%6=4... so The number 29 can represent both.

If we want just the eventual answer (4), we can just 29 // 6. That's what we'll dod on our
second pass.

The number 6 comes from the length of the list. Since all indicies/nums will be smaller than that,
it's suitable to use
"""

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i, curr in enumerate(nums):
            nxt = nums[curr] % N
            nums[i] += N * nxt
        for i in range(N):
            nums[i] //= N
        return nums

