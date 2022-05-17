"""
===== Initial Thoughts =====
[3,2,2,1,5,3,1,6,3,2,4] limit = 6

5
{1:1, 2:2, 3:0, 4:0, 5:0, 6:0}

special case == limit, and half limit (or looking for same?)
hmm doesn't quite work
6
[3,2,2,1,5,3,1,6,3,2,4]
[6,5,4,3,3,3,2,2,2,1,1]
[1,1,2,2,2,3,3,3,4,5,6]


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===
[3,3,3,2,2,2]

~~Complexity Analysis
Time - 
Space - 
"""
from collections import deque
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        queue = deque(people)
        total = 0
        while len(queue):
            num = queue.popleft()
            leftover = limit - num
            if leftover and queue and queue[-1] <= leftover:
                queue.pop()
            total += 1
        return total
