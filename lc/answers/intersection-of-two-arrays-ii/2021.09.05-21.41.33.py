"""
simple way to do this without a lot of thought would be to make a dict
of each list. Then iterate over one dict (doesn't matter) inspecting
the other for overlap. picks the lowest number of occurrences.
dict would be a mapping of num -> num_occurences

tracing:
dict1 = {1: 2, 2: 2}
dict2 = {2: 2}
seems to work

dict1 = {4: 1, 9: 1, 5: 1}
dict2 = {9: 2, 4: 2, 8: 1}
"""

from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for num in nums1:
            dict1[num] += 1
        for num in nums2:
            dict2[num] += 1
        final_items = []
        for num in nums1:
            if num not in final_items and num in dict2:
                final_items += [num] * min(dict1[num], dict2[num])
        return final_items
        