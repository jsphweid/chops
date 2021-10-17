"""
2 is prime, so we can remove multiples of 2
3 is prime, is prime so we can remove multiples of 3

n=6 2,4 => 2 0's (ceil(6/2) - 1?)
n=7 2,4,6 => 3 0's (ceil(7/2) - 1)
n=8 2,4,6 => 3 0's ()

n=10 3,6,9 => 3 0's (ceil(10/3) - 1)

"""
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        nums = [True] * n
        nums[0: 2] = [False] * 2
        count = 0
        for i, num in enumerate(nums):
            if num:
                count += 1
                nums[i::i] = [False] * (math.ceil(n / i) - 1)
        return count
