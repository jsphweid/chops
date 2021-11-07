"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        while root.left or root.right:
            curr = []
            queue = [root]
            while len(queue):
                node = queue.pop(0)
                if node.left:
                    if not node.left.left and not node.left.right:
                        curr.append(node.left.val)
                        node.left = None
                    else:
                        queue.append(node.left)
                if node.right:
                    if not node.right.left and not node.right.right:
                        curr.append(node.right.val)
                        node.right = None
                    else:
                        queue.append(node.right)
            res.append(curr)

        return res + [[root.val]]