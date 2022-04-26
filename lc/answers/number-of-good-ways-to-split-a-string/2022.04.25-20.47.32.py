"""
===== Initial Thoughts =====
seems like you can just keep a set and down counts?

"aacaba"
0 {} {abc}
1 {a} {abc}
2 {a} {abc}
3 {ac} {ab}
4 {}

The problem is it's hard to determine when you can delete a letter if there
are multiple letters of the same one left. You need counts. So just use a dict.

0 {total: 0} {a:4, b:1, c:1, total: 3}
1 {a: 1, total: 1} {a:3, b:1, c:1, total: 3}
2 {a: 2, total: 1} {a:2, b:1, c:1, total: 3}
3 {a: 2, c: 1, total: 2} {a:2, b:1, c:0, total: 2}
etc...

~~Complexity Analysis
Time - O(n)
Space - O(n)
"""
from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        res = 0
        left, right = Counter(), Counter(s)
        left_unique, right_unique = 0, len(right)
        for char in s:
            right[char] -= 1
            left[char] += 1
            if right[char] == 0: right_unique -= 1
            if left[char] == 1: left_unique += 1
            res += right_unique == left_unique
        return res







