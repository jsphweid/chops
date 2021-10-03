# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = []
        def recurse(node):
            nums.append(node.val)
            if node.left: recurse(node.left)
            if node.right: recurse(node.right)
        recurse(root)
        nums.sort()
        lowest_diff = float("inf")
        for i in range(1, len(nums)):
            lowest_diff = min(lowest_diff, abs(nums[i] - nums[i - 1]))
        return lowest_diff