from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        seen = set(deadends)
        count = -1
        while queue:
            count += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target: return count
                if node in seen: continue
                seen.add(node)
                for i in range(4):
                    num = int(node[i])
                    queue.append(node[:i] + str(0 if num == 9 else num + 1) + node[i+1:])
                    queue.append(node[:i] + str(9 if num == 0 else num - 1) + node[i+1:])
        return -1