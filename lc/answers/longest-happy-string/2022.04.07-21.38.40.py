"""
~~Complexity Analysis
Time - 3^n TLE's as expected
Space - n (?)

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        longest = ""
        def recurse(aa, bb, cc, path):
            nonlocal longest
            if len(path) > len(longest):
                longest = path
            last_two = path[-2:]
            if aa and last_two != "aa":
                recurse(aa - 1, bb, cc, path + "a")
            if bb and last_two != "bb":
                recurse(aa, bb - 1, cc, path + "b")
            if cc and last_two != "cc":
                recurse(aa, bb, cc - 1, path + "c")
        recurse(a, b, c, "")
        return longest

times out as expected

maybe if we stop early because we reach some depth...?

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
aabbaabbc

["", "", "c"]
chunk1=aa
res=aabb
"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        lst = ["a" * a, "b" * b, "c" * c]
        lst.sort(key=len, reverse=True)
        while len(lst[0]):
            chunk1 = lst[0][:2]
            res += chunk1
            lst[0] = lst[0][len(chunk1):]  # adjust

            if not len(lst[1]):
                return res

            amt_to_steal = 2 if len(lst[1]) > len(lst[0]) else 1
            chunk2 = lst[1][:amt_to_steal]
            res += chunk2
            lst[1] = lst[1][len(chunk2):]  # adjust
            lst.sort(key=len, reverse=True)
        return res

