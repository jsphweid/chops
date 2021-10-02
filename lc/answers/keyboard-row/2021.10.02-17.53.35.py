"""
===== Initial Thoughts =====
just use sets...

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set(list("qwertyuiop"))
        second = set(list("asdfghjkl"))
        third = set(list("zxcvbnm"))
        output = []
        for word in words:
            setized = set(list(word.lower()))
            if setized.issubset(first) or setized.issubset(second) or setized.issubset(third):
                output.append(word)
        return output