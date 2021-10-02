"""
===== Initial Thoughts =====
I almost remember the previous solution... not sure if it's appropriate to use since it was so hard to find initially
and it's so specific. I'll use it for now

we need the min number, max number. And then we do something with the nums in between.

[1, 2, 5]
[2, 3, 5]
[3, 4, 5]
[4, 5, 5]
[5, 6, 5]
[6, 6, 6]
5 moves

diff between the largest and smallest is 4.

[1, 2, 2, 5]
[2, 3, 3, 5]
[3, 4, 4, 5]
[4, 5, 5, 5]
[5, 6, 6, 5]
[6, 7, 6, 6]
[7, 7, 7, 7]
6 moves

diff between largest and smallest is 4 

I'm focusing on those two inner numbers

[1, 5, 5, 5]
[2, 6, 6, 5]
[3, 7, 7, 5]
[4, 7, 8, 6]
[5, 8, 8, 7]
[6, 9, 8, 8]
[7, 9, 9, 9]
[8, 10, 10, 9]
[9, 10, 11, 10]
[10, 11, 11, 11]
[11, 12, 12, 11]
[12, 12, 13, 12]
[13, 13, 13, 13]

12 moves diff between largest and smallest is 4... I notice 5 and 5 are both 4 away from smallest, 4 + 4 + 4 = 12
this seems to work for the above too... I'm going for it

"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        return sum([n - min_num for n in nums])