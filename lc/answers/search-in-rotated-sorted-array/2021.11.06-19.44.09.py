"""
===== Initial Thoughts =====
nums = [4,5,6,7,0,1,2], target = 0
l=0, r=6, m=3, v=7
l=4, r=6, m=5, v=1
l=4, r=5, m=4, v=0 return True

nums = [4,5,6,7,0,1,2], target = 3
l=0, r=6, m=3, v=7
l=4, r=6, m=5, v=1
l=4, r=5, m=4, v=0
l=5, r=5
1==3.. False

[4,5,6,7,0,1,2], target=0

l=0, r=6, m=3
l=4, r=6, m=5
l=4, r=5, m=4

[3,1] 1
l=0, r=1, m=0


if nums[mid_i] < target <= nums[r]:
3<1<
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid_i = (l + r) // 2
            if nums[mid_i] == target:
                return mid_i
            if nums[l] <= nums[mid_i]:
                # left is valid range
                if nums[l] <= target < nums[mid_i]:
                    r = mid_i
                else:
                    l = mid_i + 1
            else:
                # right is valid range
                if nums[mid_i] < target <= nums[r]:
                    l = mid_i + 1
                else:
                    r = mid_i
        return l if nums[l] == target else -1

