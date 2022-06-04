"""
===== Initial Thoughts =====
[1,2,3,4,3] + [1,2,3,4,3]
stack=[(4,3),(3,5),(4,9)]
res=[2,3,4,-1,4]

N=4
nums = [3,2,1,4,3,2,1,4]
stack = [(3,4),(4,3),(5,2), etc.]
res = [4, 4, 4, -1]

N = 3
nums = [1,2,1,1,2,1]
stack = [(1,2)]
res = [2, -1, 2]

=== Implemented Approach ===
stack, just double size, keep indices and values in stack

~~Complexity Analysis
Time - O(n)
Space - O(n)
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums = nums + nums
        res = [-1] * N
        stack = []
        for i, num in enumerate(nums):
            while stack and num > stack[-1][1]:
                ii, _ = stack.pop()
                if ii < N:
                    res[ii] = num if res[ii] == -1 else res[ii]
            stack.append((i, num))
        return res