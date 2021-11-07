"""
===== Initial Thoughts =====
mapping of rotatable digits to their rotations
convert input to string
create another new empty string and add the mapped items to it
if we encounter any items not in the mapping, we return false immediately
reverse the str we created, convert it to an int... and assert converted result
is not the original

89
8,9
"86"
"68"
68 != 89 => True

11
"11"
"11"
11 != 11 => False

25
"2 => False

60
"90"
"09"
9 != 60 => True

6
9
"""

class Solution:
    def confusingNumber(self, n: int) -> bool:
        mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        new_num = ""
        for char in str(n):
            if char not in mapping: return False
            new_num += mapping[char]
        new_num = new_num[::-1]
        return int(new_num) != n