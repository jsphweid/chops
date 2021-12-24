"""
[3,2,1,0,4]
last = 4
queue = [(3,0)]
1 2 3
(1, 1) (2, 2) (3, 3)

[2,3,1,1,4]
 0 1 2 3 4

backwards is optimal in a few cases but fatal in others
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        queue, seen = [len(nums) - 1], set()
        while queue:
            i = queue.pop()
            for j in range(i - 1, -1, -1):
                if nums[j] >= i - j and j not in seen:
                    if j == 0:
                        return True
                    queue.append(j)
                    seen.add(j)
        return False

for example... [1,1,1,1,1,1,1,1,1,1, etc.]

forward works but it's still slow...

    def canJump(self, nums: List[int]) -> bool:
        queue, last, seen = [0], len(nums) - 1, set()
        while queue:
            i = queue.pop()
            if i >= last:
                return True
            for j in range(1, nums[i] + 1):
                if i + j not in seen:
                    queue.append(i + j)
                    seen.add(i + j)
        return False

treating it like a graph is not optimal though

we should be able to go over it once

imagine we have a boost from the element of power X
continuing to the next one, we have a boost of X-1.
But the power on that element may be larger than X-1.
So we can use that instead.
If we run out and aren't at the end, the answer is false.

        power = nums[0]
        if len(nums) == 1: return True
        if not power: return False
        for i in range(1, len(nums) - 1):
            power = max(power - 1, nums[i])
            if power < 1: return False
        return True

but that's kind of messy

[0, 1]
[3,2,1,0,4] i=0 power=3
i=0 power=3
i=1 power=2
i=2 power=1
i=3 power=0

failed on 
[2,3,1,1,4] i=0 power=2
after power=2 i=1
after power=3 i=2
after power=2 i=3
after power=1 i=4
after power= needs to be >=

now failing on
[3,2,1,0,4]
after power=3 i=1
after power=2 i=2
after power=1 i=3
after power=0 i=4 actually needs to be >... or = to length instead
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        i, power = 0, nums[0]
        while power > 0 and i < len(nums):
            power = max(power - 1, nums[i])
            i += 1
        return i == len(nums)