"""
a=50
z=75

70 shift10, 55

80 - 25 => 55

70 shift100
50+shift94
50+shift68
50+shift42
50+shift16
66
94%26

failed because I fundamentally misunderstood the problem
but now I get it and I think it's a relatively small adjustmnet

s = "abc", shifts = [3,5,9]
we just need to adjust shifts
3+5+9
  5+9
    9

"""

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        acc = 0
        for i in range(len(shifts) - 1, -1, -1):
            original = shifts[i]
            shifts[i] += acc
            acc += original

        res = ""
        for char, shift in zip(s, shifts):
            distance_to_a = ord("z") + 1 - ord(char)
            if shift < distance_to_a:
                res += chr(ord(char) + shift)
            else:
                new_shift = (shift - distance_to_a) % 26
                res += chr(ord("a") + new_shift)
        return res
