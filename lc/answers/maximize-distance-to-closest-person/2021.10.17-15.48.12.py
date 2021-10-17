"""
===== Initial Thoughts =====
can do it with one pass by getting the number of 0s on the left, number of 0s on the right and max
0s in between. divide middle max by 2 round up. Then get max of left,center,right
"""
import math
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        num_left_zeros = 0
        left_zeros_done = False
        most_zeros = 0
        zeros = 0
        for i, seat in enumerate(seats):
            if seat:
                if not left_zeros_done: num_left_zeros = zeros
                left_zeros_done = True
                if zeros > most_zeros: most_zeros = zeros
                zeros = 0
            else:
                zeros += 1
        return max(num_left_zeros, math.ceil(most_zeros/2), zeros)