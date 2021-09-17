# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        calc = [root]
        output = []
        while len(calc):
            # push average
            output.append(sum(n.val for n in calc) / len(calc))
            # add children
            temp = []
            for node in calc:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            calc = temp
        return output
            