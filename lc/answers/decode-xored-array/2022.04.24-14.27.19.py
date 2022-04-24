"""
===== Initial Thoughts =====
000 - 0
001 - 1
010 - 2
011 - 3
100 - 4
101 - 5
110 - 6
111 - 7

[1,2,3]

0 ^ 0 = 0
1 ^ 0 = 1
0 ^ 1 = 1
1 ^ 1 = 0

opposite of xor is "bits must be the same"
[1,]

Hmm... it's just an equation
encoded[i] = arr[i] XOR arr[i + 1]

encoded = [1,2,3], first = 1

so: 1=1^x... using my equation above.
do the opposite of xor 1 to both sides
1 !^ 1 => 0

we know the next number is 0.
res=[1,0,_,_]
now 2=0^x
do !^0 to both sides
2 !^ 0 => ??? 2

res=[1,0,2,_]
now 3=2^x
do !^2 to both sides
3 !^ 2 wouldn't I get 6

Wait !^ == ^ ??
1^1=>0
2^0=>2
3^2=>1
"""

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for num in encoded:
            res.append(res[-1] ^ num)
        return res