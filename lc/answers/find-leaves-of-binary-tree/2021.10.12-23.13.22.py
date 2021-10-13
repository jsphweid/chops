"""
=== Brute Force Approach ===
brute force would be finding those leaves then deleting before recursing further down.
Then start over again from the top

~~Complexity Analysis
Time - n log n? where n is the number of nodes?
Space - O(n * height)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        nums = []
        def disconnect_leaves(node):
            disconnected_nodes = []
            if node.left:
                if not node.left.left and not node.left.right:
                    disconnected_nodes.append(node.left.val)
                    node.left = None
                else:
                    disconnected_nodes.extend(disconnect_leaves(node.left))
            if node.right:
                if not node.right.left and not node.right.right:
                    disconnected_nodes.append(node.right.val)
                    node.right = None
                else:
                    disconnected_nodes.extend(disconnect_leaves(node.right))
            return disconnected_nodes
        while root.left or root.right:
            nums.append(disconnect_leaves(root))
        return nums + [[root.val]]

            