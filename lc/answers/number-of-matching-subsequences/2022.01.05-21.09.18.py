"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 


s = "abcde", words = ["a","bb","cd","ace"]
char=b
i=5


def is_subsequence(needle: str, haystack: str) -> bool:
    i = 0
    for char in needle:
        while i < len(haystack) and haystack[i] != char:
            i += 1
        if i == len(haystack):
            return False
        else:
            i += 1
    return True

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res, memo = 0, {}
        for word in words:
            if word not in memo:
                memo[word] = is_subsequence(word, s)
            res += memo[word]
        return res

S = "abcde"
count = 1
words = ["a", "bb", "acd", "ace"]
a: [["a"], ["c", "d"], ["a", "c", "e"]]
b: [["b", "b"]]
"""

from collections import defaultdict, deque

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d, count = defaultdict(deque), 0
        for word in words:
            w = deque(word)
            d[w[0]].append(w)
        for char in s:
            for _ in range(len(d[char])):
                word = d[char].popleft()
                word.popleft()
                if word:
                    d[word[0]].append(word)
                else:
                    count += 1
        return count
















