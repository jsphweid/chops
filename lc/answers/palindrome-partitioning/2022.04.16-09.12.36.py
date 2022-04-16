"""
===== Initial Thoughts =====
aab, each char by itself is a palindrome
aa b

abbababa
abba b a b a

["a","b","b","a","b","a","b","a"],
["a","b","b","a","b","aba"],
["a","b","b","a","bab","a"],
["a","b","b","aba","b","a"],
["a","b","b","ababa"],
["a","b","bab","a","b","a"],
["a","b","bab","aba"],
["a","b","babab","a"],
["a","bb","a","b","a","b","a"],
["a","bb","a","b","aba"],
["a","bb","a","bab","a"],
["a","bb","aba","b","a"],
["a","bb","ababa"],
["abba","b","a","b","a"],
["abba","b","aba"],
["abba","bab","a"]]

We should be able to solve this recursively.
a + b + others
a + bb + others

aab
recurse("aab", [])
    recurse("ab", ["a"])
        recurse("b", ["a", "a"])
            recurse("", ["a", "a", "b"])
    recurse("b", ["aa"])
        recurse("", ["aa", "b"])

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: return []
        self.res = []
        self.recurse(s, [])
        return self.res

    def recurse(self, s: str, path):
        if not s:
            self.res.append(path)
        for i in range(len(s)):
            section = s[:i+1]
            if self.is_palindrome(section):
                self.recurse(s[i+1:], path + [section])

    def is_palindrome(self, s: str):
        N = len(s)
        for i in range(N // 2):
            if s[i] != s[N - i - 1]:
                return False
        return True

let's try to make it one function for fun...
partition("aab", [])
    partition("ab", ["a"]) -> [["a", "a", "b"]]
        partition("b", ["a", "a"]) -> [["a", "a", "b"]]
            partition("", ["a", "a", "b"]) -> [["a", "a", "b"]]
    partition("b", ["aa"]) -> [["aa", "b"]]
        partition("", ["aa", "b"]) -> [["aa", "b"]]

[["a", "a", "b"]]
"""

class Solution:
    def partition(self, s: str, path=[]) -> List[List[str]]:
        if not s: return [path]
        res = []
        for i in range(len(s)):
            t = s[:i+1]
            good = True
            for j in range(len(t) // 2):
                if s[j] != s[len(t) - j - 1]:
                    good = False
                    break
            if good:
                res.extend(self.partition(s[i+1:], path + [t]))
        return res
