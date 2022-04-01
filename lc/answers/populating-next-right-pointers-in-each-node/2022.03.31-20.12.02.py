"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        queue = deque([root])
        while queue:
            N = len(queue)
            for i in range(N):
                node = queue.popleft()
                if node.left and node.right:  # it's perfect
                    queue.extend([node.left, node.right])
                node.next = queue[0] if i < N - 1 else None
        return root

but how can we do it without extra space?
connect(1, None)
    connect(3, None)? (has 6 after going right)
        connect(7, None)? (7 next is None) -> 7
        connect(6, 7) (6 next is 7) -> 6

Only got this far... 
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]', nxt=None) -> 'Optional[Node]':
        if not root: return
        node = None
        if root.left and root.right:
            node = self.connect(root.right, None)
            node = self.connect(root.left, node)
        root.next = nxt
        return root if not root.left and not root.right else node

going to read discussions because I've spent a lot of time (42 minutes)
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        queue = deque([root])
        while queue:
            N = len(queue)
            for i in range(N):
                node = queue.popleft()
                if node.left and node.right:  # it's perfect
                    queue.extend([node.left, node.right])
                node.next = queue[0] if i < N - 1 else None
        return root
