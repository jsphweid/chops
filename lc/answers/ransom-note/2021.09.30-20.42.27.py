from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = defaultdict(int)
        for char in magazine: counts[char] += 1
        for char in ransomNote:
            if char in counts and counts[char]:
                counts[char] -= 1
            else:
                return False
        return True