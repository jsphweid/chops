"""
===== Initial Thoughts =====
can't be greedy because
[1,7,10] = 14

so BFS should do

~~Complexity Analysis
Time - 
Space - 
"""
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = set()
        queue = deque([amount])
        num_coins = -1
        while queue:
            num_coins += 1
            for _ in range(len(queue)):
                left = queue.popleft()
                if left == 0:
                    return num_coins
                for coin in coins:
                    new_amount = left - coin
                    if new_amount >= 0 and new_amount not in seen:
                        seen.add(new_amount)
                        queue.append(new_amount)
        return -1
