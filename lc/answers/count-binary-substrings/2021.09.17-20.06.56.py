class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        streak = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                count += 1
                streak = 1
            else:
                if streak:
                    streak += 2
                    if i - streak >= 0 and s[i - streak] != s[i]:
                        count += 1
                    else:
                        streak = 0
        return count