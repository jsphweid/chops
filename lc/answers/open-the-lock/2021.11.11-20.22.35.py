"""
===== Initial Thoughts =====
deadends = ["0201","0101","0102","1212","2002"]
0202 to 0202
0000 to 0202
0210

0000

ending conditions
ran into a deadend -> don't record count
arrived at solution -> have count

0000
    1000
    9000
    0100
    0900
    0010
    0090
    0001
    0009


=== Brute Force Approach ===
work out every possible path with recursion... but ran into out of memory errors
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        min_length = float("inf")
        up = {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '0'}
        down = {'9': '8', '8': '7', '7': '6', '6': '5', '5': '4', '4': '3', '3': '2', '2': '1', '1': '0', '0': '9'}
        def dfs(curr, length=0):
            nonlocal min_length
            if curr == target:
                min_length = min(length, min_length)
                return
            if curr in deads:
                return
            if length > min_length:
                return
            as_list = list(curr)
            for i in range(8):
                index_to_modify = i // 2
                as_list[index_to_modify] = up[as_list[index_to_modify]] if i & 1 else down[as_list[index_to_modify]]
                dfs("".join(as_list), length + 1)
        dfs("0000", 0)
        return -1 if min_length == float("inf") else min_length


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===
after reading an example online, I think this might work if we use iteration
instead

~~Complexity Analysis
Time - 
Space - 
"""
from collections import deque

up = {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '0'}
down = {'9': '8', '8': '7', '7': '6', '6': '5', '5': '4', '4': '3', '3': '2', '2': '1', '1': '0', '0': '9'}


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        height = -1
        queue = deque(["0000"])
        while queue:
            height += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target: return height
                if node in deads: continue
                deads.add(node)
                for i, char in enumerate(node):
                    queue.append(node[:i] + up[char] + node[i + 1:])
                    queue.append(node[:i] + down[char] + node[i + 1:])
        return -1