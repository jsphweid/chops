"""
===== Initial Thoughts =====
You can divide components 09f166 -> 09 f1 66 then find the closest for each that has the same 
hex digit. For example, 66 doesn't need to change because it's already in that format.
The closest number to 09 is 11 in hex. The closest number to f1 is ee in hex.

Given f1, how do we find the closest? We could increase f1 until you get the double letter (ff)
and decrease until it's a double letter (ee) and compare the distances of each, going with the
shorter. If you did it this way, I doubt you'd even need the equation.

It'd be annoying to loop over f1, f2, f3, etc. just to find ff though. I wonder what the
mathematical significance of ff or ee is...
0x00 = 0
0x11 = 17
0x22 = 34
0x33 = 51
0x44 = 68
0x55 = 85
0x66 = 102
0x77 = 119
etc.

Also note that 0xff // 16 => 15 (which is `f` 0-indexed)
I wonder if we can round up/down to 14 or 15

something like round(int('f7', 16) / 16) might just do it...
I played around with this but got some unexpected results. This isn't 10/20/30, it's 11/22/33

for i in range(16):
    print((" {:02x}" * 17).format(*range(i * 17, (i * 17) + 17)))

 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10
 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 20 21
 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32
 33 34 35 36 37 38 39 3a 3b 3c 3d 3e 3f 40 41 42 43
 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50 51 52 53 54
 55 56 57 58 59 5a 5b 5c 5d 5e 5f 60 61 62 63 64 65
 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76
 77 78 79 7a 7b 7c 7d 7e 7f 80 81 82 83 84 85 86 87
 88 89 8a 8b 8c 8d 8e 8f 90 91 92 93 94 95 96 97 98
 99 9a 9b 9c 9d 9e 9f a0 a1 a2 a3 a4 a5 a6 a7 a8 a9
 aa ab ac ad ae af b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 ba
 bb bc bd be bf c0 c1 c2 c3 c4 c5 c6 c7 c8 c9 ca cb
 cc cd ce cf d0 d1 d2 d3 d4 d5 d6 d7 d8 d9 da db dc
 dd de df e0 e1 e2 e3 e4 e5 e6 e7 e8 e9 ea eb ec ed
 ee ef f0 f1 f2 f3 f4 f5 f6 f7 f8 f9 fa fb fc fd fe
 ff

Looks like we actually need to do add one and divide by 17. The 17 is because each row has 17
I'm not entirely sure why we need to add one immediately but it might be related to the offset
of the whole scale having 1 extra (i.e. 17 instead of 16)

round((int('f6', 16)+1) / 17)

=== Implemented Approach ===
Use a math-based function to round the nums appropriately.

~~Complexity Analysis
Time - O(1)
Space - O(1)

REFLECTION:
I failed once because of the bogus +1. I eliminated it and it worked. Not sure why I thought it
should go there but it was my downfall... 
Upon further reflection, I realize I put it there because the midpoint was always a little off.
But when I actually counted the nums between the midpoint and the end, it turned out to be a bit
different than I expected.
"""

class Solution:
    def similarRGB(self, color: str) -> str:
        ret = "#"
        h = "0123456789abcdef"
        for i in [1, 3, 5]:
            hex_num = color[i: i + 2]
            pos = round(int(hex_num, 16) / 17)
            ret += h[pos] * 2
        return ret


