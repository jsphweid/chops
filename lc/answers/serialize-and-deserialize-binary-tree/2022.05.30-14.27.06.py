"""
=== Brute Force Approach ===
just use json?

=== Implemented Approach ===
import json
class Codec:

    def serialize(self, root):
        def dictify(node):
            if not node: return {}
            d = {"v": node.val}
            if not node.left and not node.right:
                return d
            d["l"] = dictify(node.left)
            d["r"] = dictify(node.right)
            return d
        return json.dumps(dictify(root))

    def deserialize(self, data):
        def construct(d):
            if "v" not in d:
                return None
            node = TreeNode(d["v"])
            node.left = construct(d.get("l", {}))
            node.right = construct(d.get("r", {}))
            return node
        return construct(json.loads(data))

But read some solutions... Now I'm going to try preorder
"""

import json
class Codec:

    def serialize(self, root):
        lst = []
        def preorder(node):
            if node:
                node.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                lst.append("#")
        return lst.join(" ")


    def deserialize(self, data):
        
