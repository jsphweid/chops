"""
===== Initial Thoughts =====
What a wonderfully simply problem that is probably not too easy

[1,1,2,1,1], k = 3
result = 2

[1,1,1,1,1], k = 3, result = 3
[1,1,1,1], k = 3, result = 2
[1,1,1], k = 3, result = 1

[1,1,1,1,1,1], k = 3, result = 4


7
[2,2,2,1,2,2,1,2,2,2], k = 2

=== Brute Force Approach ===
single pass to convert items to just 1s and 0s
then use 2 for loops to sum up all odds

~~Complexity Analysis
Time - O(n^3)
Space - O(n)

=== Implemented Approach ===
So I tried a more 'two-pointer' approach that failed, but I think I can improve on the brute force
(or at least my last brute force) and take it from n^3 to n^2. We shouldn't have to do that sum...



~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        simple = [n & 1 for n in nums]
        count = 0
        for i in range(len(nums)):
            start_count = 0
            for j in range(i, len(nums)):
                start_count += simple[j]
                if start_count == k:
                    count += 1
        return count
