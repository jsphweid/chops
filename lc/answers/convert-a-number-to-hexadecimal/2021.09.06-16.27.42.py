"""
trivial with a built-in

actually this is tough because python doesn't get constrained by 32 bit ints

I read a bit but not a lot. We have to take into account 2's compliment.

-1 is always 1111111 or ffff etc.

000 0
001 1
010 2
011 3
100 -4
101 -3
110 -2
111 -1

3 bits lets us have -4 to 3 or [-2**2 <= num <= 2**2 - 1]

if we have 1111, we can get hex from that pretty easily
"0123456789abcdef"
we can just shift 4 bits and convert. That works for positive numbers but not negative though, right?

Actually after playing around in the repl, I think we can do the same for both positive and negative
numbers... We just have to have a good cut off.
"""

class Solution:
    def toHex(self, num: int) -> str:
        output = ""
        hex_chars = "0123456789abcdef"
        bits_to_shift = 28

        # a 32 bit to number can be bit shifted (in increments of 4) 8 times
        for _ in range(8):
            char = hex_chars[0xF & (num >> bits_to_shift)]
            bits_to_shift -= 4
            if output or char != "0":
                output += char
        return output or "0"

