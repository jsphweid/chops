"""

my original solution was a brute force.....

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

reading discussions now.......

Ya, my approach isn't too far off -- I knew you had to serialize and use set/dict to do lookup
but my basic fault is that it's extremely expensive for mine to serialize each node. Ideally you
shouldn't have to traverse all the way down to serialize a different node.

Reading Stefan P's answer made me think of how git hashes contents. You can INCLUDE hashes
as part of the contents to "include the whole history" (the history itself is used as part of)
the hash. 

We could do that here if we did DFS.

We get to the end and hash the leaf, then the parent's hash can include
the leaf hashes. And the grandparent's hash can include the parent's hashes, etc.
So you don't have to explore all the children over and over to make a new unique hash. You just
use THEIR hash...
"""

from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        everything = defaultdict(list)

        def hash_it(node):
            this_hash = str(hash("None"))
            if node:
                this_hash = str(hash(str(node.val) + hash_it(node.left) + hash_it(node.right)))
                everything[this_hash].append(node)
            return this_hash

        hash_it(root)

        return [e[0] for e in everything.values() if len(e) > 1]

