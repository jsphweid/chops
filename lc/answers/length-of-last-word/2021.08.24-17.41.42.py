class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for word in reversed(s.split(" ")):
            if word:
                return len(word)