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
"""
char=1 prev="1", count=1
char=2 prev="2", count=1
char=1 prev="1", count=1
char=1 prev="1", count=2
"""
def count_chars(s: str):  # "1211" -> [(1, '1'), (1, '2'), (2, '1')]
    groups = []
    count = 0
    previous_char = None
    for char in s:
        if previous_char:
            if previous_char != char:
                groups.append((count, previous_char))
                count = 1
                previous_char = char
            else:
                count += 1
        else:
            previous_char = char
            count = 1
    if count:
        groups.append((count, previous_char))
    return groups

# 1211 ([(1, '1'), (1, '2'), (2, '1')]) -> 111221 
def compute_next(curr: str):
    s = ""
    for count, char in count_chars(curr):
        s += str(count) + char
    return s

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        base = "1"
        for _ in range(n - 1):
            base = compute_next(base)
        return base
