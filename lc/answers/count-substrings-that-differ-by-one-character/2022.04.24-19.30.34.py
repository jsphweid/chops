"""
===== Initial Thoughts =====
s = "aba", t = "baba"
whatabout a simpler example
s = "a", t = "baba"
"a" -> "b" in two locations.
doing it for one character is easy
it's basically the length of the other str minus the number of that char

but we have to consider all the substrings...
abcd  bbcd

=== Brute Force Approach ===
get all substrings.
iterate over all those changing each character to be another character
adding how many times that substring exists

~~Complexity Analysis
Time - verrrrrrrrrrry bad

=== Implemented Approach ===
thing is, when considering a short substring, if that one doesn't work
then neither will a longer one.

But how do we efficiently check if a substring is in another

abcdefg  abcdffgh
abcde abcdf 
    differs by 1, and all shorter do too
        bcde bcdf, cde cdf, de df, e f
but you can go further
    abcdef abcdff, abcdefg abcdffg, each time adding many more
    once we hit 1 diff, we start counting

Also how do we count?
We know if two strings are equal "abc", "abc" 1+2+3

"aba", "baba"
 a      b       1 diff (+1)
 ab     ba      2 diffs
  b      a      1 diff (+1)
  ba     ab     2 diffs
   a      b     1 diff (+1)
--------------
 a       a      0 diff
 ab      ab     0 diff
 aba     aba    0 diff
--------------
 a        b     1 diff (+1)
 ab       ba    2 diffs
  b        a    1 diff (+1)

but it misses 1... the last a on first string and first b on second string
if the two strings were longer, it'd miss many more.

Is there anything to consider in the counts approach? The major problem
is that it'll work for substrings of length 1, but not longer ones. 

s = "aba", t = "baba"
t_counts = {b: 2, a: 2}
aba
a    -> 4-2 (4 total - 2 a's) => 2
 b   -> 4-2 (4 total - 2 b's) => 2
  a  -> 4-2 (4 total - 2 a's) => 2
2+2+2 = 6... but that only works because no substrings longer than 1 match

s = "ab", t = "bb"
t_counts = {b: 2}
ab 
a   -> 2-0 (2 total - 0 a's) => 2
b   -> 2-2 (2 total - 2 b's) => 0
2+0 = 2

But answer is 3

Maybe if we counted substrings greater than 1... but that'll be an explosion
d = {1: {"b": 2}
     2: {"bb":1}}

This is brute force.

But it's all I got...
[{"b": 2}, {"bb": 1}]
0
    1
    2
1
    2
[{b: 2, a: 2}, {ba: 2, ab: 1}, {bab: 1, aba: 1}, {baba: 1}]
Failed because my brain is not thinking clearly. I'm pretending
this is another problem for some reason.

from collections import defaultdict
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        lookup = [defaultdict(int) for _ in range(len(t))]
        for i in range(len(t)):
            for j in range(i+1, len(t)+1):
                lookup[j - i - 1][t[i:j]] += 1
        res = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                res += lookup[j - i - 1][s[i:j]]
        return res

Read a solution in discussions... just do brute force.
"""

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        res, M, N = 0, len(s), len(t)
        for i in range(M):
            for j in range(N):
                k = wrong = 0
                while i + k < M and j + k < N and wrong < 2:
                    wrong += s[i + k] != t[j + k]
                    res += wrong == 1
                    k += 1
        return res
