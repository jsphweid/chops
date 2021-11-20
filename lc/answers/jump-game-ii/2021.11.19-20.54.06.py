from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        seen = {0}
        queue = deque([0])
        level = -1
        while len(queue):
            level += 1

            for _ in range(len(queue)):
                i = queue.popleft()
                val = nums[i]
                if i == N - 1:
                    return level
                elif i + val >= N - 1:
                    return level + 1

                for j in range(1, min(val + 1, N - i)):
                    nxt = i + j
                    if nxt not in seen:
                        queue.append(nxt)
                        seen.add(nxt)
