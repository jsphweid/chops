"""
return true if all rules are true:
- num capitals is 0
- num capitals is length of str
- num capitals is 1 and first letter is capital
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        num_capitals = sum([1 if c == c.upper() else 0 for c in word])
        if num_capitals == 0 or num_capitals == len(word):
            return True
        if num_capitals == 1 and word[0] == word[0].upper():
            return True
        return False
