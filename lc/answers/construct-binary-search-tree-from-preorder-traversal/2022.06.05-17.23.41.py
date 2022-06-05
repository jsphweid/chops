"""
===== Initial Thoughts =====
should be able to do this recursively and also using a stack

note this is only possible because it is a BST and not just a BT

I can't really think of the recursive solution and I'm wasting a ton of time...

Let's think about a monotonic stack...
[ 8, 5, 1, 7,10,12]
[10, 7, 7,10,12,-1]

even this is hard...

going back to recursion.

Needed help on this one. The recursion of lee215 was almost exactly 
what I was thinking... I just couldn't execute...

[8,5,1,7,10,12]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0
        def build(bound):
            nonlocal i
            if i == len(preorder) or preorder[i] > bound:
                return None
            node = TreeNode(preorder[i])
            i += 1
            node.left = build(node.val)
            node.right = build(bound)
            return node
        return build(float("inf"))