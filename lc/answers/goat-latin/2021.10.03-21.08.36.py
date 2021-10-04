"""
=== Implemented Approach ===
iterate through the words applying the rules, paying special attention to case. Have a handle to 1. whether first letter
is vowel or not and 2. index that its on

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ret = ""
        words = sentence.split(" ")
        for i, word in enumerate(words):
            base = word if word[0].lower() in {"a", "e", "i", "o", "u"} else f"{word[1:]}{word[0]}"
            suffix = "ma" + ("a" * (i + 1))
            ret += base + suffix + ("" if (i == len(words) - 1) else " ")
        return ret