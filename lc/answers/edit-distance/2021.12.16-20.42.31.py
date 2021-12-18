"""
replace a character
    - we'd only want to replace a character with something in word2
insert a character
    - similar to the above

there's no reason to insert a character when we have enough characters
    - because we can change a character

we have to delete when the lengths aren't the same
we have to insert when the lengths aren't the same

intention -> execution, both are 9 characters, 5/9 are different

horse -> ros
hor
hos
hoe
hrs
hre
hse
... etc
one of them will be close... within 1 letter change of ros


"z" -> "ros"
change + 2 adds

"o" -> "ros"
2 adds

--------
word1 = "horse", word2 = "ros"

h -> change to r (change)
h -> put a r in front of it (append)
h -> delete the h (if deleting is possible) (delete)
h -> leave the h (if we have room left?!)

horse ros

rorse, orse
rosse, rose, hrse, rse
rose, ros
ros

we need to keep track of the temp word and the index it's on

rose roase
string[:i] + string[i] + string[i+1:]

(horse, ros)
(orse, os) (orse, ros)
(se, s) (sse, s) (rrse, ros) (rse, ros)
(e, )

(horse, ros)
"""
from collections import deque
from math import inf
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        root = (word1, word2)
        queue, seen, depth, lowest = deque([root]), set(), -1, inf
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                left, right = node

                while left and right and left[0] == right[0]:
                    left = left[1:]
                    right = right[1:]

                if not left and not right:
                    lowest = min(lowest, depth)
                    continue

                # there is something in each, and they are different!

                candidates = []
                if right:
                    candidates.append((right[0] + left[1:], right))
                    candidates.append((right[0] + left, right))
                candidates.append((left[1:], right))

                for candidate in candidates:
                    if candidate not in seen:
                        seen.add(candidate)
                        queue.append(candidate)
        return lowest

"""

(horse, ros)
(orse, os) (orse, ros)
(se, s) (sse, s) (rrse, ros) (rse, ros)
(e, )
"""




