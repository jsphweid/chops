class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output = []
        queue = [root]
        buffer = []
        while len(queue) or len(buffer):
            if len(queue):
                buffer.append(queue.pop())
            else:
                total = 0
                length = len(buffer)
                for node in buffer:
                    total += node.val
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                output.append(total / length)
                buffer = []
        return output