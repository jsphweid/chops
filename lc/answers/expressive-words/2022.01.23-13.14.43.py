"""
last=e
ooooo
pupppp
puppp

"dddiiiinnssssssoooo"
["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]

Like others, I misunderstood the question:
https://leetcode.com/problems/expressive-words/discuss/123308/Some-test-case-have-problems

My solution was pretty terrible anyways.

def is_expressive(s, word):
    if len(s) < len(word): return False
    x, y, last, streak = 0, 0, None, 0
    while x < len(s) and y < len(word):
        if s[x] == word[y]:
            if streak == 1:
                return False
            else:
                streak = 0
            last = word[y] 
            x += 1
            y += 1
        else:
            if s[x] == last:
                x += 1
                streak += 1
            else:
                return False
    return (s[x:] == last * len(s[x:])) and (len(s[x:]) + streak != 1)

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return sum([is_expressive(s, w) for w in words])

So I really liked the four pointer solution as it's the easiest to understand and debug.
"""

def is_expressive(s, w):
    i, i2, j, j2, m, n = 0, 0, 0, 0, len(s), len(w)
    while i < m and j < n:
        while i2 < m and s[i2] == s[i]: i2 += 1
        while j2 < n and w[j2] == w[j]: j2 += 1
        if s[i] != w[j]: return False
        if i2-i != j2-j:
            if i2-i < 3: return False
            if j2-j > i2-i: return False
        i, j = i2, j2
    return i == m and j == n



class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return sum([is_expressive(s, w) for w in words])
