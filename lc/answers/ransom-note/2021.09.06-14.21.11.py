"""
I think the double dict approach is a good way to solve this. I can think of a few other ways
but not sure they are faster.
"""
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = defaultdict(int)
        magazine_dict = defaultdict(int)
        for char in ransomNote:
            ransom_dict[char] += 1
        for char in magazine:
            magazine_dict[char] += 1
        for key, val in ransom_dict.items():
            if magazine_dict[key] < val:
                return False
        return True