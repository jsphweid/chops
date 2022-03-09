from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([root])
        res = []
        while queue:
            last_index = len(queue) - 1
            for i in range(len(queue)):
                node = queue.popleft()
                if i == last_index:
                    res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res