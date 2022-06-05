"""
===== Initial Thoughts =====
Input: nums = [1,2,3,2]
Output: 14

we want to increase the minimum but also increase sum

Input: nums = [2,3,3,1,2]
Output: 18

Input: nums = [3,1,5,6,4,2]
Output: 60

=== Brute Force Approach ===
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = -float("inf")
        N = len(nums)
        for i in range(N):
            total = 0
            minimum = float("inf")
            for j in range(i, N):
                minimum = min(minimum, nums[j])
                total += nums[j]
                res = max(res, minimum * total)
        return res % ((10**9) + 7)

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== Implemented Approach ===
After reading discussions... use monotonic stack

~~Complexity Analysis
Time - O(n)
Space - O(n)

[ 0  1  2  3  4  5] indices
[ 3, 1, 5, 6, 4, 2]
[ 3, 4, 9,15,19,21] sums
[ 1, 6, 4, 4, 5, 6] next small
[-1,-1, 1, 2, 1, 1] prev small

[ 1, 6, 2, 1, 3, 4] diff
"""

def make_sums(nums):
    res = []
    for num in nums:
        res.append(res[-1] + num if res else num)
    return res

def make_next_small(nums):
    N = len(nums)
    res = [N] * N
    stack = []
    for i, n in enumerate(nums):
        while stack and n < stack[-1][1]:
            ii, _ = stack.pop()
            res[ii] = i
        stack.append((i, n))
    return res


def make_prev_small(nums):
    N = len(nums)
    res = [-1] * N
    stack = []
    for i in range(N - 1, -1, -1):
        n = nums[i]
        while stack and n < stack[-1][1]:
            ii, _ = stack.pop()
            res[ii] = i
        stack.append((i, n))
    return res


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        sums = make_sums(nums)
        next_small = make_next_small(nums)
        prev_small = make_prev_small(nums)

        res = -float("inf")
        for i, n in enumerate(nums):
            # pretend this is the lowest
            left = 0 if prev_small[i] == -1 else sums[prev_small[i]]
            right = sums[next_small[i] - 1]
            res = max(res, n * (right - left))
        return res % ((10**9) + 7)
