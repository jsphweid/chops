"""
I'll brute force it like the other one but there's definitely a better way
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSum(self, root):
        if not root:
            return 0
        return root.val + self.getSum(root.left) + self.getSum(root.right)


    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = 0
        queue = [root] if root else []
        while len(queue):
            node = queue.pop(0)
            total += abs(self.getSum(node.left) - self.getSum(node.right))
            if node.left and (node.left.left or node.left.right):
                queue.append(node.left)
            if node.right and (node.right.left or node.right.right):
                queue.append(node.right)
        return total
