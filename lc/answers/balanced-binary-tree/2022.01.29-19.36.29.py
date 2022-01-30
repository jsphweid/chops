"""
failed first time because I didn't consider non-nodes

failed a few more times... I'm not really sure this can be accomplished iteratively, easily at least...

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        queue, heights = [(root, 0)], []
        while queue:
            node, height = queue.pop()
            if not node.left and not node.right:
                heights.append(height)
            if node.left: queue.append((node.left, height + 1))
            if node.right: queue.append((node.right, height + 1))
        return abs(max(heights) - min(heights)) < 2 if heights else True

[3,9,20,null,null,15,7]
[1,2,2,3,3,null,null,4,4]
[]
[1,null,2,null,3]

[1,2,3,4,5,6,null,8]
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def get_height(node, height=0):
            nonlocal is_balanced
            if not node or (not node.left and not node.right):
                return height
            left = get_height(node.left, height + 1) if node.left else height
            right = get_height(node.right, height + 1) if node.right else height
            if abs(left - right) > 1:
                is_balanced = False
            return max(left, right)
        get_height(root)
        return is_balanced