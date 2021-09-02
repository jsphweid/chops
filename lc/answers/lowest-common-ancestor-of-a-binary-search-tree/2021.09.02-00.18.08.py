# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		max_val = max(p.val, q.val)
		min_val = min(p.val, q.val)

		while True:
			if root.val == p.val or root.val == q.val:
				return root
			if min_val < root.val and max_val > root.val:
				return root
			if root.val > max_val:
				root = root.left
			elif root.val < min_val:
				root = root.right
