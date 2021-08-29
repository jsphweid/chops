"""
This should be fairly easy to do in a recursive way. The basic strategy would work like this:
find the midpoint in the list. That's the current node. To get the left and right nodes, simply
recurse calling it each side with the subset of nums on the left and subset of nums on right
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

        midpoint_index = len(nums) // 2
        midpoint_value = nums[midpoint_index]
        left_tree = self.sortedArrayToBST(nums[0:midpoint_index])
        right_tree = self.sortedArrayToBST(nums[midpoint_index+1:len(nums)])
        return TreeNode(val=midpoint_value, left=left_tree, right=right_tree)
