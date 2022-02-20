"""
===== Initial Thoughts =====
We can easily build a graph.

~~Complexity Analysis
Time - O(2^n)
Space - O(n)

fn([1,1,1], 2)
    fn([1,1], 3)
        fn([1], 4)
            fn([], 5)
            fn([], 3)
        fn([1], 2)
            fn([], 1)
            fn([], 3)
    fn([1,1], 1)
        fn([1], 0)
            fn([], -1)
            fn([], 1)
        fn([1], 2)
            fn([], 1)
            fn([], 3)

So of course that TLEs
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return target == 0
        return self.findTargetSumWays(nums[1:], -nums[0] + target) + \
            self.findTargetSumWays(nums[1:], nums[0] + target)

We should be able to add caching -- if a path gets to the same
sum by a seen num, we know we can just ADD ON its value as well.

To start, let's switch to an iterative approach.

Here's essentially the same thing written iteratively.

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        stack, seen, res = [(0, 0)], dict(), 0
        while stack:
            i, total = stack.pop()
            if i == len(nums):
                res += total == target
            else:
                stack.append((i + 1, total + nums[i]))
                stack.append((i + 1, total - nums[i]))
        return res

Then finally we'll add caching. This is a little trickier because
we need to point multiple intermediaries at one answer.

Failed on this unexpectedly.
[0,0,0,0,0,0,0,0,1]
1

The reason this doesn't work is because this aggressive caching assumes
that each path will be unique enough. But in this example, the +/- result
in the same thing. So we have to count it twice.

Caching doesn't make a lot of sense here I've discovered.

This example is interesting because 256 is just 2^8... There are 9
numbers. 2^9 is 512 but only half of them go in the correct direction
on the last num.

One idea is to use the cache solution but just remove the 0s before hand. Then
add them back at the end by multiplying the result by 2^n where n is the num
of 0s.

Passed the test above, but tests still probably TLEing and failing on this one:
[9,7,0,3,9,8,6,5,7,6]
2

Oof. Now I'm really confused. This example is too big to easily understand
what is going on.

I was doing some whiteboarding and realized that you can just do half of the
space then count inversions but it only saves 1 layer. Turns 2^n into 2^(n-1)
or something like that.

I'm guessing the answer is something DP. But I'm going to look at the discussions
as I'ved wasted too much time.


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        original_length = len(nums)
        nums = [n for n in nums if n != 0]
        num_zeros = original_length - len(nums)

        stack, seen, res = [[(0, 0)]], dict(), 0
        while stack:
            paths = stack.pop()
            i, total = paths[-1]
            if i == len(nums):
                works = total == target
                res += works
                for i, total in paths:
                    seen[(i, total)] = works
            else:
                if (i, total) in seen:
                    res += seen[(i, total)]
                else:
                    stack.append(paths + [(i + 1, total + nums[i])])
                    stack.append(paths + [(i + 1, total - nums[i])])
        return res * (2 ** num_zeros)

So I should've just added caching to my solution.

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int, seen=None) -> int:
        if not seen:
            seen = {}
        if not nums:
            return target == 0
        key = (target, len(nums))
        if key in seen:
            return seen[key]
        res = self.findTargetSumWays(nums[1:], -nums[0] + target, seen) + \
            self.findTargetSumWays(nums[1:], nums[0] + target, seen)
        seen[key] = res
        return res
"""
    
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int, seen=None) -> int:
        if seen == None:
            seen = {}
        if not nums:
            return target == 0
        key = (target, len(nums))
        if key in seen:
            return seen[key]
        res = self.findTargetSumWays(nums[1:], -nums[0] + target, seen) + \
            self.findTargetSumWays(nums[1:], nums[0] + target, seen)
        seen[key] = res
        return res
