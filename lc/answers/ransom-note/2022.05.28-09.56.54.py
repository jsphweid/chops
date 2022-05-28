from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)
        for char in ransomNote:
            if counts[char] > 0:
                counts[char] -= 1
            else:
                return False
        return True