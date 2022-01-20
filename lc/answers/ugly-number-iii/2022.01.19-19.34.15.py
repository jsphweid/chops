"""
4 2 3 4

4 4 4

failed once because I'm double counting...
        def find_total_smaller(num):
            return sum([num // z for z in [a, b, c]])

if num//a and num//b return the same thing, we need to not count it twice
we need to take out their LCM

n=5 a=2 b=3 c=3
3 6
[2,3,4,6,8]
4+2 - 3 => 3 (go higher, that's why it's bad)

original
the problem is that if we're going to set(2,3,3), we can't make lcms for 3,3
left=1 right=20 mid=10

6 2 1 3
nums=[2,1,3] lcms=[2,3,6]
3+6+2 3+2+1
1 2 3 4 5 6 7

Man I'm struggling with this seemingly simple problem...
Apparently on top of all my other failures, I had forgotten that the LCM of 6 and 8 is not 48
"""
import math
def get_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def get_lcms(nums):
    if len(nums) < 2:
        return []
    if len(nums) == 3:
        return [get_lcm(nums[0], nums[1]), get_lcm(nums[1], nums[2]), get_lcm(nums[0], nums[2])]

    # then there must be two
    return [get_lcm(nums[0], nums[1])]

def process(a, b, c):
    a, b, c = sorted([a, b, c])
    res = [a]
    if b % a != 0:
        res.append(b)
    if c % a != 0 and c % b != 0:
        res.append(c)
    return res

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        nums = process(a, b, c)
        lcms = get_lcms(nums)
        def find_total_smaller(num):
            return sum([num // p for p in nums]) - sum([num // p for p in lcms])
        left, right = 1, 2000000000
        while left < right:
            mid = (left + right) // 2
            if find_total_smaller(mid) >= n:
                right = mid
            else:
                left = mid + 1
        return left