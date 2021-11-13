from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([root])
        maxes = []
        while queue:
            max_num = -float("inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                max_num = max(node.val, max_num)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            maxes.append(max_num)
        return maxes