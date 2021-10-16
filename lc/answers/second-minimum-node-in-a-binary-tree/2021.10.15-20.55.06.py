class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s = set()
        def recurse(node):
            if not node: return
            s.add(node.val)
            recurse(node.left)
            recurse(node.right)
        recurse(root)
        l = sorted(s)
        return -1 if len(l) == 1 else l[1]