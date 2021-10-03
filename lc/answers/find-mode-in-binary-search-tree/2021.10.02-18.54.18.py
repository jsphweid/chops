# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = defaultdict(int)
        def recurse(node):
            counts[node.val] += 1
            if node.left: recurse(node.left)
            if node.right: recurse(node.right)
        recurse(root)
        max_num = max(counts.values())
        return [val for val in counts.keys() if counts[val] == max_num]