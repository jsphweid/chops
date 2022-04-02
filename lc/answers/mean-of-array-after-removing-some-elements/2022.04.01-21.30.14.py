"""
=== Brute Force Approach ===
solution would be to sort, then remove elements from beginning and end

~~Complexity Analysis
Time - O(nlogn)
Space - O(n) - for producing a copy with slice

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        cut = len(arr) // 20
        return sum(arr[cut: len(arr) - cut]) / (len(arr) - cut - cut)