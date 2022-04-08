"""
haystack = "hello", needle = "ll"
i=2
j=1

hell
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        if haystack == "": return -1
        for i in range(len(haystack)):
            found = True
            if len(needle) + i > len(haystack):
                return -1
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    found = False
                    break
            if found:
                return i
        return -1