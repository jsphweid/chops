class Solution:
    def countSegments(self, s: str) -> int:
        trimmed_str = s.strip()
        if not trimmed_str:
            return 0
        if len(trimmed_str) == 1:
            return 1
        count = 1
        for i in range(1, len(trimmed_str)):
            if trimmed_str[i] == " ":
                count += 0 if trimmed_str[i - 1] == " " else 1
        return count