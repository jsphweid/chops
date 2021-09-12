"""
we could just store the rows as sets and check to make sure the lowercased words are all contained within a
single one of those sets
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = set("qwertyuiop")
        middle = set("asdfghjkl")
        bottom = set("zxcvbnm")
        ret = []
        for word in words:
            s = set(word.lower())
            if s.issubset(top) or s.issubset(middle) or s.issubset(bottom):
                ret.append(word)
        return ret
