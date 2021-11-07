"""
===== Initial Thoughts =====
1 => 1
2 => 11
3 => 21
4 => 1211
5 => 111221
6 => 312211
7 => 13112221
8 => 1113213211
9 => 31131211131221

"1" 
1. [('1', '1')] "11"
2. [('11', '1')] "21"
3. [('2', '2'), ('1', '1')] "1211"
take what's on the third iteration

=== Brute Force Approach ===
count up using their logic

~~Complexity Analysis
Time - 
Space - 
"""
import re
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        base = "1"
        for _ in range(n - 1):
            new_str = ""
            for group, char in re.findall(r"((.)\2*)", base):
                new_str += str(len(group)) + char
            base = new_str
        return base
