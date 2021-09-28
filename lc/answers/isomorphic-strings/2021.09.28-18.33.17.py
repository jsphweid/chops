"""
===== Initial Thoughts =====
My first solve gave me a lot of trouble, but I recall it's easier than I think.

=== Implemented Approach ===
keep a dictionary of mappings. if we encounter a char in s, then assert its value in the dict (if it exists) is
equal to the corresponding t char. If it's not, return false. If it's not in mapping, then add it.

~~Complexity Analysis
Time - O(n) where n is the length of s/t
Space - O(2n) because the dict and set might have to store all the chars
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()
        for left, right in zip(s, t):
            if left in mapping:
                if mapping[left] != right:
                    return False
            else:
                if right in used:
                    return False
                mapping[left] = right
                used.add(right)
        return True