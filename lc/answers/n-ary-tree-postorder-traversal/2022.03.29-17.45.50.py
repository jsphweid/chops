class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []
        for c in root.children:
            res.extend(self.postorder(c))
        res.append(root.val)
        return res
