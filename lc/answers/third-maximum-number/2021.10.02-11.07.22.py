"""
===== Initial Thoughts =====
should be pretty easy with a SortedSet (which I haven't used before but hey... I'm 
sure it's legal on a google interview...?)

=== Brute Force Approach ===
turn nums into a set. then turn into a list. sort it. if len is at least 3,
then get -3 from end, else get -1.

honestly, maybe this can be done with one pass over nums... probably. Will try that next
time probably.
"""
from sortedcontainers import SortedSet
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = SortedSet(nums)
        return s[-1] if len(s) < 3 else s[-3]