"""
===== Initial Thoughts =====
[6,3,2,8,6,5,3]
[6,3,3,8,6,5,2]

[1,1,5]
i=1
j=2


[1,2,3]
i=1
breaking_num=2
j=2

diff=3-2,1
next_largest_diff=1 next_largest_pos=2

                nums[next_largest_pos] = nums[i]
                nums[i] = next_largest_diff
                [1,2,2]

[2,3,1]

i=0

i=0 j=2 diff=1-2

[3,1,2]

"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # find the breaking point
        i = len(nums) - 2
        while i > -1:
            if nums[i] < nums[i + 1]:
                # find the next largest and swap
                breaking_num = nums[i]
                j = len(nums) - 1
                next_largest_pos = None
                next_largest_diff = float('inf')
                while j > i:
                    diff = nums[j] - breaking_num
                    if 0 < diff < next_largest_diff:
                        next_largest_diff = diff
                        next_largest_pos = j
                    j -= 1
                # TODO: no next largest diff?
                next_largest_num = nums[next_largest_pos]
                nums[next_largest_pos] = nums[i]
                nums[i] = next_largest_num
                break
            i -= 1

        # reverse every after breaking point
        l = i + 1
        r = len(nums) - 1
        while l < r:
            r_num = nums[r]
            nums[r] = nums[l]
            nums[l] = r_num
            l += 1
            r -= 1

