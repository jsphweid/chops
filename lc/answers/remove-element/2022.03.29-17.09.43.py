"""
===== Initial Thoughts =====
two pointer
[0,1,2,2,3,0,4,2]
 0 1 3 0 4 2 2 2 

[0,1,3,0,4,2,2,2]
           l
2 2 2 2 => 0

[2,2,3,3]
     l

~~Complexity Analysis
Time - O(n)
Space - O(1)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for i, num in enumerate(nums):
            if num != val:  # i.e. it's good
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        return left