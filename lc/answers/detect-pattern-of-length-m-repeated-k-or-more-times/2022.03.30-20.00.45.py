"""
=== Brute Force Approach ===
same approach as last time...
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - (m * k) + 1):
            if arr[i:i+m] * k == arr[i:i+(m*k)]:
                return True
        return False

=== Implemented Approach ===
But now let's do a one pass, this is tricky!
[1,2,3,1,2,3,1,2,3] need 6 (3 repeat 3) (stop 6)
[1,2,1,2,1,3] need 4 (2 repeat 3) (stop 4?) len-2
[1,2,1,2,1,1,1,3] need 2 (2 repeat 2) (stop 7) len-2
[1,2,4,4,4,4] need 3 ? (1 repeat 4)
~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        bar = m * k - m
        streak = 0
        for i in range(len(arr) - m):
            if arr[i] == arr[i + m]:
                streak += 1
                if streak == bar:
                    return True
            else:
                streak = 0
        return False
