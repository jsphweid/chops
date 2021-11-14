from collections import deque
from math import inf
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([root])
        res = []
        while queue:
            highest = -inf
            for _ in range(len(queue)):
                node = queue.popleft()
                highest = max(node.val, highest)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(highest)
        return res