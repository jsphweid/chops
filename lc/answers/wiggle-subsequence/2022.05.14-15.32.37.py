"""
===== Initial Thoughts =====
DP

~~Complexity Analysis
Time - O(N^2) with DP key index + up/down should only have 2x? right?
Space - O(N)
"""

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dfs(i, need_up):
            longest = 1
            for j in range(i + 1, N):
                if (need_up and nums[j] > nums[i]) or (not need_up and nums[j] < nums[i]):
                    longest = max(longest, 1 + dfs(j, not need_up))
            return longest

        return max(dfs(0, True), dfs(0, False))
