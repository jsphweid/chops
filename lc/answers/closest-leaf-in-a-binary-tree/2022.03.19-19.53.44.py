"""
===== Initial Thoughts =====
I think the term tree is deceptive here since it can find a leaf
by going any way. I.E. we have to connect both ways. Not sure if
there are loops, but we can just use a 'seen' in case.

=== Implemented Approach ===
Make an adj list and do bfs starting from the request node.
Return as soon as you find the first leaf.

~~Complexity Analysis
Time - O(N) where N is the number of nodes
Space - O(N)

{1: [2,3], 2: [1,4], 3: [1], 4: [2,5], 5: [4,6], 6: [5]}

failed on [1,3,2] k=1
{1: [2,3], 2: [1], 3: [1]}
[3], {1}

[1,2]
1
{1:[2], 2:[1]}
"""
from collections import defaultdict, deque
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        if not root.left and not root.right:
            return root.val

        adj = defaultdict(list)
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [node.left, node.right]:
                if child:
                    adj[node.val].append(child.val)
                    adj[child.val].append(node.val)
                    stack.append(child)

        queue, seen = deque([k]), set()
        while queue:
            val = queue.popleft()
            if len(adj[val]) == 1 and val != root.val: return val
            if val in seen: continue
            seen.add(val)
            queue.extend(adj[val])


