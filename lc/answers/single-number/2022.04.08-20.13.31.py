"""
===== Initial Thoughts =====
some two pass is probably the solution

[2,2,1] => [4,4,2]
[4,1,2,1,2] (10) => [8,2,4,2,4]

FAILED TO GET IN 10 MINUTES

the one solution was not two pass, but xor... go figure

I guess I could've thought "how do we cancel numbers out?"

1100 xor
1100
-----
0000

xor with 0 leaves the number basically

~~Complexity Analysis
Time - O(n)
Space - O(1)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res