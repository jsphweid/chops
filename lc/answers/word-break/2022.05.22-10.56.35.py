"""
===== Initial Thoughts =====
use trie and graph

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

trie = {
    a: { n: { d: { *: True } } }
    c: { a: { t: {
                *: True,
                s: { *: True } } } },
    d: { o: { g: { *: True } } }
    s: { a: { n: { d: { *: True } } } }
}

trie = {
    a: { n: { d: { *: True } } }
    c: { a: { t: {
                *: True,
                s: { *: True } } } },
    d: { o: { g: { *: True } } }
    s: { a: { n: { d: { *: True } } } }
}
queue=[0]
"catsandog"
i=0
"""
from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        for word in wordDict:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr["*"] = True

        seen = set()
        queue = deque([0])
        while queue:
            i = queue.popleft()
            curr = trie
            while i < len(s) and s[i] in curr:
                curr = curr[s[i]]
                i += 1
                if "*" in curr and i not in seen:
                    if i == len(s):
                        return True
                    seen.add(i)
                    queue.append(i)
        return False


