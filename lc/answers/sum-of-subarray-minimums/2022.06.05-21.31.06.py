"""
===== Initial Thoughts =====
I came across this problem from another problem in one of lee215's write-ups.
It can be accomplished with monotonic stacks and counting from each point.
[3,1,2,4]
starting at 3... how many subarrays are there where 3 is the minimum
       with 1... how many subarrays are there where 1 is the minimum
       etc.

You can answer these by finding the number to the left and the right that are smaller.
[3 , 1,2,4]
[-1,-1,1,2] (indices of next smallest on left)
[ 1, 4,4,4] (indices of next smallest on right)
  1, 4,2,1

  1 -> 1 => 1
  2 -> 1+2 => 3
  3 -> 1+2+3 => 6
  4 -> 1+2+3+4 => 10

I'm kinda stuck... I don't really know how to calculate this.

Hmm... left and right need to be independent.
3 -> 0 on left, 0 on right, and itself (0+0+1) - 1
1 -> 1 on left, 2 on right, and itself (1+3+1) - 5
2 -> 0 on left, 1 on right, and itself (0+1+1) - 2
4 -> 0 on left, 0 on right, and itself (0+0+1) - 1

That's not quite right...

I need to look at the discussions.
My mistake is calculating the number of subarrays with that minimum.
I was trying to use the triangle to arrive at it but all I really needed to do
was multiply the numbers. This doesn't really make sense to me but obviously works.

TODO: research this more?

~~Complexity Analysis
Time - O(n)
Space - O(n)
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        left = [-1] * N
        right = [N] * N

        stack = []
        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                ii, _ = stack.pop()
                right[ii] = i
            stack.append((i, n))
        stack = []
        for i in range(N - 1, -1, -1):
            n = arr[i]
            while stack and n <= stack[-1][1]:
                ii, _ = stack.pop()
                left[ii] = i
            stack.append((i, n))

        total = 0
        for (i, n), l, r in zip(enumerate(arr), left, right):
            total += n * (i - l) * (r - i)
        return total % ((10**9) + 7)
