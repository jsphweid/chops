"""
===== Initial Thoughts =====
get s splitted into segments
if length of pattern isn't the length of splitted, return False
zip through them adding new pairs to some map. if existing pair, assert equals...
pair is a 1 way mapping

~~Complexity Analysis
Time - O(2n), once to split, the the other zip pass
Space - O(4n), storing the whole thing as list but also the map, which worst case 2n (each entry is a pair), + set (post-failure)
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitted = s.split(" ")
        if len(pattern) != len(splitted): return False
        mapping = {}
        used_words = set()
        for char, word in zip(pattern, splitted):
            if char in mapping:
                if mapping[char] != word:
                    return False
            else:
                if word in used_words:
                    return False
                mapping[char] = word
                used_words.add(word)
        return True