"""
~~Complexity Analysis
Time - O(n)
Space - O(n)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
root=new1
seen={1: new1, 2: new2}
recurse(old1, new1)
    recurse(old2, new2)
        recurse(old3, new3)
    recurse(old4, new4)
    etc.
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        seen = {}
        def recurse(old, new):
            new.val = old.val
            new.neighbors = []
            seen[new.val] = new
            for child in old.neighbors:
                if child.val in seen:
                    new.neighbors.append(seen[child.val])
                else:
                    new_child = Node()
                    recurse(child, new_child)
                    new.neighbors.append(new_child)

        root = Node()
        recurse(node, root)
        return root
