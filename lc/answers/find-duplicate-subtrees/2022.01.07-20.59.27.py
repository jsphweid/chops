from collections import defaultdict

def serialize_tree(root):
    res, queue = "", [root]
    while queue:
        node = queue.pop()
        left = node.left.val if node.left else "N"
        right = node.right.val if node.right else "NZ"
        res += str(node.val) + str(left) + str(right)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return res


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        d, queue = defaultdict(list), [root]
        while queue:
            node = queue.pop()
            d[node.val].append(node)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        res = []
        for nodes in d.values():
            s, added = set(), set()
            for node in nodes:
                serialized = serialize_tree(node)
                if serialized in s and serialized not in added:
                    res.append(node)
                    added.add(serialized)
                else:
                    s.add(serialized)
        return res

