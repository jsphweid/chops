"""
=== Implemented Approach ===
just use dictionaries to store counts of each. Then iterate over 1 and get counts in each, selecting the
minimum and pushing it to the list that many

~~Complexity Analysis
Time - O(2m + n)
Space - O(m + n)
"""
from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for n in nums1: dict1[n] += 1
        for n in nums2: dict2[n] += 1
        ret = []
        for n in dict1.keys(): ret.extend([n] * min(dict1[n], dict2[n]))
        return ret