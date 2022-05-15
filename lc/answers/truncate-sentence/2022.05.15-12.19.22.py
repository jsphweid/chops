class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        spaces = 0
        for i, char in enumerate(s):
            if char == " ":
                spaces += 1
                if spaces == k:
                    return s[:i]
        return s