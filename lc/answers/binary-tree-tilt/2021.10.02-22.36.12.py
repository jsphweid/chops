"""
===== Initial Thoughts =====
I still don't know if I have a better solution for this.
I think we can have an inner recursive function that adds tilts to a global list. But we need to "iterate"
through each 

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
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def get_sum(node):
            total = node.val
            if node.left: total += get_sum(node.left)
            if node.right: total += get_sum(node.right)
            return total
        total = 0
        queue = [root]
        while len(queue):
            node = queue.pop()
            left_sum = get_sum(node.left) if node.left else 0
            right_sum = get_sum(node.right) if node.right else 0
            total += abs(left_sum - right_sum)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return total
