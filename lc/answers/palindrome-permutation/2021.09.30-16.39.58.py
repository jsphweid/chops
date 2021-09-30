"""
=== Brute Force Approach ===
make every possible permutation and return true if any one of them is a palindrome

not sure on the complexity of permutations/combinations exactly yet

=== Implemented Approach ===
count chars. there can only be one odd char.

~~Complexity Analysis
Time - O(2n)
Space - O(n)
"""
from collections import defaultdict
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = defaultdict(int)
        for char in s: counts[char] += 1
        odd_found = False
        for val in counts.values():
            if val & 1:
                if odd_found:
                    return False
                odd_found = True
        return True