"""
===== Initial Thoughts =====
I was working on a medium that was pretty difficult and in one of the discussions
`maximum-subarray-min-product`
it mentioned that this problem could be a precursor

I've been recently thinking about monotonic stacks more. Their use seems to be
easily summarized with "could next/prev increasing/decreasing element be useful here"

In this problem, if we had knowledge at each spot in the list where the next
and prev decreasing element occurred, we could easily answer what the largest rectangle
is in the histogram

=== Implemented Approach ===
use a monotonic stack

~~Complexity Analysis
Time - O(n)
Space - O(n)

(i, val)
2, 6, 10, 6, 8, 3
heights =  [2, 1, 5, 6, 2, 3]
next_small=[1, 6, 4, 4, 6, 6]
prev_small=[-1,-1,1, 2, 1, 4]
stack=[]
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        next_small, prev_small = [N] * N, [-1] * N
        stack = []
        for i, h in enumerate(heights):
            while stack and h < stack[-1][1]:
                ii, _ = stack.pop()
                next_small[ii] = i
            stack.append((i, h))

        stack = []
        for i in range(N - 1, -1, -1):
            h = heights[i]
            while stack and h < stack[-1][1]:
                ii, _ = stack.pop()
                prev_small[ii] = i
            stack.append((i, h))

        res = -float("inf")
        for i in range(N):
            l = next_small[i] - prev_small[i] - 1
            res = max(res, heights[i] * l)
        return res
