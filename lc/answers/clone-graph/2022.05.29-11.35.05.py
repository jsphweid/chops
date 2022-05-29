"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        copy = Node(node.val)
        neighbors_copy = []
        for n in node.neighbors:
            neighbors_copy.append(self.cloneGraph(n))
        copy.neighbors = neighbors_copy
        return copy

honestly this probably works for a tree but not a graph...

the hard thing is loops that are common in graphs

I think we could simply build an adj list and then make a copy from that

1: [2,4]
2: [1,3]
3: [2,4]
4: [1,3]
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if not node.neighbors:
            return Node(node.val)
        adj = defaultdict(list)
        stack = [node]
        while stack:
            n = stack.pop()
            if n.val not in adj:
                for c in n.neighbors:
                    adj[n.val].append(c.val)
                    stack.append(c)

        lookup = {val: Node(val) for val in adj.keys()}
        for copy_val, neighbor_vals in adj.items():
            copy = lookup[copy_val]
            copy.neighbors = []
            for nv in neighbor_vals:
                copy.neighbors.append(lookup[nv])

        return lookup[node.val]

