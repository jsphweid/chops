"""
===== Initial Thoughts =====
two four loops should be decent here. It's never ideal putting loops inside loops, but I don't think it's
that bad here considering the sizes get smaller.

the try/catch is a bad idea... not every out of range means instant failure... if the corresponding out of range
also exists, then it's good!!!

for now, let's prefill with any char

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        longest_word = max(map(len, words))
        if len(words) != longest_word: return False
        filled_words = [w + ("x" * (longest_word - len(w))) for w in words]
        for i in range(len(filled_words) - 1):
            for j in range(i + 1, len(filled_words)):
                if filled_words[i][j] != filled_words[j][i]:
                    return False
        return True