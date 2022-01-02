class Solution:
    def maxPower(self, s: str) -> int:
        streak, longest, last_char = 1, 1, s[0]
        for i in range(1, len(s)):
            if last_char == s[i]:
                streak += 1
            else:
                longest = max(longest, streak)
                last_char = s[i]
                streak = 1
        longest = max(longest, streak)
        return longest