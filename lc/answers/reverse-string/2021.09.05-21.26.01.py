"""
since we have to do this in-place, we could have two pointers that start at each end
and get closer to each other, temporarily holding the values and swapping them

for even lengthed problems the swapping would stop before they crossed
[0, 1, 2, 3, 4, 5] ->
0 - 5
1 - 4
2 - 3 DONE (stops at 3)

6//2 = 3

for odd lengthed problems, the swapping should stop at the half
[0, 1, 2, 3, 4]
0 - 4
1 - 3 DONE (stops at 2)

5//2 => 2 midpoint

Actually, in either case it can simply go up to the midpoint so we don't need anything special for the 
stopping part
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            left_index = i
            right_index = len(s) - 1 - i
            left_char = s[left_index]
            right_char = s[right_index]
            s[left_index] = right_char
            s[right_index] = left_char