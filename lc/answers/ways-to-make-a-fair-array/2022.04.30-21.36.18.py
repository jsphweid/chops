"""
===== Initial Thoughts =====
[6,1,7,4,3] -> 1
total evens = 16
total odds = 5
[6,6,13,13,16] (evens on left inclusive)
[0,1,1,5,5] (odds on left inclusive)

[16,10,10,3,3] (evens on right inclusive)
[5,5,4,4,0] (odds on right inclusive)
so if we remove index 1,
we know it is [6,7,4,3] where evens are 10 and odds are 10, so that's our good one

when we remove the 1 index, our numbers left stay the same
but on right, odds turn even and even turn odd
BUT we also have to ditch the one we're currently on

6 evens / 4 right after shift
0 odds / 10 right after shift

I'm not sure we have to ditch the one we're currently on... because I think
it'll balance out...

~~Complexity Analysis
Time - O(n)
Space - O(n)
(2 6 4)
FAILED On [2,1,6,4]
[2,2,8,8] (evens on left inclusive)
[5,5,4,4] (odds on right inclusive)

[8,6,6,0] (evens on right inclusive)
[0,1,1,5] (odds on left inclusive)
evens = 2 + 4 
odds = 0 + 6
"""
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        N = len(nums)
        evens_left, evens_right, odds_left, odds_right = [0] * N, [0] * N, [0] * N, [0] * N
        for i, num in enumerate(nums):
            if i == 0:
                evens_left[0] = num
            else:
                evens_left[i] = evens_left[i - 1] + (0 if i & 1 else num)
                odds_left[i] = odds_left[i - 1] + (0 if i % 2 == 0 else num)
        for i in range(N - 1, -1, -1):
            num = nums[i]
            if i == N - 1:
                if N % 2 == 0:
                    odds_right[i] = num
                else:
                    evens_right[i] = num
            else:
                evens_right[i] = evens_right[i + 1] + (0 if i & 1 else num)
                odds_right[i] = odds_right[i + 1] + (0 if i % 2 == 0 else num)
        return sum([(odds_left[i] + evens_right[i]) == (evens_left[i] + odds_right[i]) for i in range(N)])