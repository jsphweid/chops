"""
~~Complexity Analysis
Time - O(n)
Space - O(n)
"""

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        lookup = {p[0]: i for i, p in enumerate(pieces)}
        i = 0
        while i < len(arr):
            val = arr[i]
            if val not in lookup:
                return False
            sublist = pieces[lookup[val]]
            if sublist != arr[i: i + len(sublist)]:
                return False
            i += len(sublist)
        return True
