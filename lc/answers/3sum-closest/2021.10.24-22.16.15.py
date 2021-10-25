"""

[-4,-1,1,2,5,12] - sorted

s's
[-4, 2, 7, 8]

3
1, 4


[0,2,1,-3]
1

[-3,0,1,2]
-2, 3

"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = sum(nums[:3])
        best_diff = abs(target - best)
        for i in range(len(nums) - 2):
            # do binary search to find a better
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                this_diff = abs(target - s)
                if this_diff < best_diff:
                    best = s
                    best_diff = this_diff
                if s < target:
                    left += 1
                else:
                    right -= 1
        return best