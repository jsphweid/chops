# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        all_leaves = []
        def disconnect_leaves(node):
            leaves = []
            if node.left and not node.left.left and not node.left.right:
                leaves.append(node.left.val)
                node.left = None
            if node.right and not node.right.left and not node.right.right:
                leaves.append(node.right.val)
                node.right = None
            if node.left: leaves.extend(disconnect_leaves(node.left))
            if node.right: leaves.extend(disconnect_leaves(node.right))
            return leaves
        while root.left or root.right:
            all_leaves.append(disconnect_leaves(root))
        return all_leaves + [[root.val]]
