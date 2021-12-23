"""
===== Initial Thoughts =====
baabb
ba a bb
3b 2a
aaaabbbb => 2
4:4
aaaabaa

bbbb



=== Brute Force Approach ===
move inward but add to another list once done

~~Complexity Analysis
Time - something log... ?
Space - O(n)

s="bb" res=2 buffer=""
0 1
baaa
"abbaaaa" 1
baaa 2
b 3

looked at answers, now I feel dumb. If it's already a palindrome, it's 1... else it's 2
"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
