"""
recursive
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        highest = (-float("inf"), 0)
        for i, num in enumerate(nums):
            highest = max(highest, (num, i))
        val, i = highest
        node = TreeNode(val)
        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i+1:])
        return node



arr = [3,2,1,6,0,5]
stack = [Node(6),]
6 -> 0
"""

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < node.val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

