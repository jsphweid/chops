"""
===== Initial Thoughts =====
brute force seems simple

=== Brute Force Approach ===
have two pointers. the difference between the indices is 1 diminension while the minimum of the two
values is the others. you just multiply those together

    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                res = max(res, (j - i) * (min(height[i], height[j])))
        return res

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== Implemented Approach ===
to optimize it, we could exit early if we know it'll never work out
That still reaches time limit exceeded.

Thinking about this more, a bar has some max value depending on its position and height. But it won't necessarily give us exact numbers
without doing an exhaustive search, right?
Like [1,8,6,2,5,4,8,3,7]
1   8   6   2   5   4   8   3   7
8   56  36  10  20  12  16  3   0
0   8   12  6   20  20  48  21  56

or [4,3,2,1,4]
4   3   2   1   4
16  9   4   1   0
0   3   4   3   16

or [1,2,1]
1   2   1
2   2   0
0   2   2

in all these cases, we get the highest number by finding the highest number in the first, then the second, take those indices and multiply heir
values in the real list and get the result... that's it.

My intuition tells me that this approach doesn't work out. It should highlight where the answer probably is around but may or may not
yield the correct answer...

Let's try it anyways..

fails on [1,8,6,2,5,4,8,25,7]

SO I read the answer... the solution is to use a 2 pointer approach. The intuition makes sense to me
as being a valid strategy that gets a lot of close results to the top but I wouldn't think that it
covers all the bases. I guess it does... let's just implement it and I'll think about it more the
next time i have to solve this problem
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            current = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

