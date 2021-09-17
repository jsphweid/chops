"""
It's not immediately clear to me if duplicate values exist...
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root: TreeNode, num: int):
        node = root
        while True:
            if node.val == num:
                return node
            if num > node.val:
                if not node.right:
                    return None
                node = node.right
            else:
                if not node.left:
                    return None
                node = node.left

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = [root]
        while len(queue):
            node = queue.pop(0)
            compliment = k - node.val
            found = self.find(root, compliment)
            if found and found is not node:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False


