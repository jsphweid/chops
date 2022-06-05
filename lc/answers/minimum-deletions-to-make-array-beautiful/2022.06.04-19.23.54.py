"""
===== Initial Thoughts =====
nums = [1,1,2,2,3,3]

nums=[1,2,2,3]

nums = [1,1,2,3,5]
[1,2,2,3,3,4,4]
[1,1,2,2,3,3,4,4]
[1,2,2,3,3,4]
[2,1,5,3,4,1,2,6]

=== Implemented Approach ===
I thinnnk.. it's just a simple stack problem where we only add the next if it
can be added. And delete one at the end if not even when finished.

~~Complexity Analysis
Time - O(n)
Space - O(n)

nums = [1,1,2,3,5]
       [1,2,3,5]

[1,1,2,2,3,3]
[1,2,2,3,3]
6-5 + True
1 + 1
2
"""

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if stack and stack[-1] == num and len(stack) & 1:
                continue
            else:
                stack.append(num)
        return len(nums) - len(stack) + (len(stack) & 1)
