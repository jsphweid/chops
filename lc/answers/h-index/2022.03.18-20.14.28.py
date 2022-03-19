"""
===== Initial Thoughts =====
[3,0,6,1,5]
[0,1,3,5,6]
[5,5,5,5,5,5,5]
[1,1,3]
[1,1,1,1,1,1]
[9,9]

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        res = 1
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] < res:
                break
            res += 1
        return res - 1