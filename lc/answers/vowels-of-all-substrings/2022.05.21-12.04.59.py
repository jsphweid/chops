"""
===== Initial Thoughts =====
abba -> 8
a b b a
ab bb ba
abb bba
abba

think about it from the right
a spawns 1, because there is 1 a
ba spawns 1, since we know while b is no vowel, it has 1 vowel still in substring
bba spawns 1, since we know hwile b in no vowel, it has 1 vowel still in substring
abba spawns 5, since we know we still have 1 vowel in previous substring, we're also adding 4 more

abab -> 10
a b a b
ab ba ab
aba bab
abab

b spawns 0
a spawns 2
b spawns 2
a spawns 4+2

aabb -> 10
a a b b
aa ab bb
aab abb
aabb

b spawns 0
b spawns 0
a spawns 3
a spawns 4 + 3

class Solution:
    def countVowels(self, word: str) -> int:
        N = len(word)
        total = curr = 0
        for i in range(N - 1, -1, -1):
            if word[i] in {"a", "e", "i", "o", "u"}:
                curr += N - i
            total += curr
        return total

but can we go from the beginning...?
abba
1115
"""

class Solution:
    def countVowels(self, word: str) -> int:
        N = len(word)
        total = curr = 0
        for i in range(N):
            if word[i] in {"a", "e", "i", "o", "u"}:
                curr += i + 1
            total += curr
        return total
