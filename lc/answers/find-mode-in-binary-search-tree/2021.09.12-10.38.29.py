# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        all_values = []
        nodes = [root]
        while len(nodes):
            node = nodes.pop(0)
            all_values.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)


        d = defaultdict(list)
        for val in set(all_values):
            count = all_values.count(val)
            d[count].append(val)
        return d[max(d.keys())]
