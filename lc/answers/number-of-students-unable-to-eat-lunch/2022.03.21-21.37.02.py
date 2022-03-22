"""
===== Initial Thoughts =====
solve through simulation?

we basically need to have some counter i that scans across sandwiches. We should probably
make `students` a deque so we can add/remove from first/last in constant time.

Can we get ourselves into an infinite loop?

If we can't go further we stop and count the number of sandwiches left.

students = [0,1], sandwiches = [0,1]

students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
{1: 3, 0: 0}

[1,1,1,0,0,0] [1,0,0,1,1,1] (should be 1)
{1:0, 0:1}

We can use a Counter but just need to think about whether or not that works globally.

[1,1,0,0], sandwiches = [0,1,0,1]
{1: 0, 0: 0}


students = [1,1,1], sandwiches = [0,1,1]


~~Complexity Analysis
Time - 
Space - 
"""
from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)
        for sandwich in sandwiches:
            if counts[sandwich]:
                counts[sandwich] -= 1
            else:
                break
        return counts[0] + counts[1]

