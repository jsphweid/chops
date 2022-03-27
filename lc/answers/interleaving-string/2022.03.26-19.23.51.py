"""
===== Initial Thoughts =====
probably a graph problem
can be solved with recursion
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"

"" "" ""

"ab" "ac" "aabc"

s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

"ab" "ac" "aabc"
fn("ab", "ac", "aabc")
    fn("b", "ac", "abc")
        fn("b", "ac", "abc") -> False
    fn("ab", "c", "abc")
        fn("ab", "c", "abc")
            fn("b", "c", "bc")
                fn("", "c", "c")
                    fn("", "", "")
"""

@cache
def fn(s1: str, s2: str, s3: str):
    if not s1 and not s2 and not s3:
        return True
    if not s3:
        return False
    # there is something in s3
    res1 = fn(s1[1:], s2, s3[1:]) if s1 and s1[0] == s3[0] else False
    res2 = fn(s1, s2[1:], s3[1:]) if s2 and s2[0] == s3[0] else False
    return res1 or res2

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return fn(s1, s2, s3)




