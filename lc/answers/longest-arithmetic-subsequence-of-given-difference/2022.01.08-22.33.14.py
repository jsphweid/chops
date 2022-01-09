"""
===== Initial Thoughts =====
[1,5,7,8,5,3,4,2,1,-1,4,2] -2
{5:1, 7:1, 8:1, 5:2, 3:3, 1:4, -1:5, 4:1, 2:2}

[1,3,5,7] 1
{1:1, 3:1, 5:1, 7:1}

[1,2,3,4] 1
{1:1, 2:2, 3:3, 4:4}

~~Complexity Analysis
Time - O(n)
Space - O(n)
"""

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = dict()
        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
        return max(dp.values())