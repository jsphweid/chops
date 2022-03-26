"""
best solution...
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, lst, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        return TreeNode(val=lst[mid], 
            left=self.helper(lst, start, mid - 1),
            right=self.helper(lst, mid + 1, end))

but I'll try with slices
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        return TreeNode(val=nums[mid], 
            left=self.sortedArrayToBST(nums[:mid]),
            right=self.sortedArrayToBST(nums[mid + 1:]))

