# the key here is that `x <= 231 - 1`... why would they write it that way?
# can I use a calulator? I'm using a calculator

# 1 -> 1... 1*1=1
# 2 -> 1... 1*1=1, 2*2=4 (which is over 2)
# 4 -> 2... 2*2=4
# 8 -> 2... 2*2=4, 3*3=9 (which is over 8)
# 226 -> 15... 16*16=? (definitely over 226)

# After failing twice, I just realized that my Leetcode Console printed 
# it out as `x <= 231 - 1` instead of `x <= 2^31 - 1`, which kind of changes everything...
# Here was my initial dumb solution
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         i = 15
#         while i >= 0:
#             if i * i <= x:
#                 return i
#             i = i - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while True:
            if i * i > x:
                break
            i = i + 1
        return i - 1