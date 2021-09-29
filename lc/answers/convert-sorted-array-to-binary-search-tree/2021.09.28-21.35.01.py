"""
I think I'll use the same approach as last time... recursion
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not len(nums):
            return None
        mid_index = len(nums) // 2
        left = self.sortedArrayToBST(nums[:mid_index])
        right = self.sortedArrayToBST(nums[mid_index + 1:])
        return TreeNode(nums[mid_index], left=left, right=right)