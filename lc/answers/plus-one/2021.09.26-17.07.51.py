"""
===== Initial Thoughts =====
How could we solve this with counting?

=== Implemented Approach ===
We could pop things off the end, and insert them into
a different list (at position 0). We need to carry properly. If number is 9, it becomes 0, but carry
is set to True. Once we use the carry, it is set to False. If at the end we still have a carry, add
a 1.

We can start `carry` as True since we need to add 1...


~~Complexity Analysis
Time - O(n)
Space - O(n)
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        carry = True
        while len(digits):
            digit = digits.pop()
            if carry:
                digit += 1
                carry = False
            if digit == 10:
                digit = 0
                carry = True
            output.insert(0, digit)
        if carry: output.insert(0, 1)
        return output

