"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {i: n for i, n in enumerate(nums)}


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        short_d, long_d = (self.d, vec.d) if len(self.d) < len(vec.d) else (vec.d, self.d)
        for i, n in short_d.items():
            if i in long_d:
                res += (n * long_d[i])
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)