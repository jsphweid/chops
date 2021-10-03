"""
=== Brute Force Approach ===
make index dict of each list
iterate over overlapping keys making a sum dict
find the min value of the values
iterate through sum dict and return all that have that value
"""
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1, l2 = {}, {}
        for i, item in enumerate(list1): l1[item] = i
        for i, item in enumerate(list2): l2[item] = i
        common_keys = set(l1.keys()).intersection(set(l2.keys()))
        overlap = {k: l1[k] + l2[k] for k in common_keys}
        winning_num = min(overlap.values())
        return [k for k, v in overlap.items() if v == winning_num]
