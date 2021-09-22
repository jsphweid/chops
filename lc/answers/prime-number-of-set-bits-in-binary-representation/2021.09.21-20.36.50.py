"""
get inclusive range
convert each num to binary and count 1's
see increment some counter if the number of 1s is prime


"""

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_map = {
            0: 0,
            1: 0,
            2: 1,
            3: 1,
            4: 0,
            5: 1,
            6: 0,
            7: 1,
            8: 0,
            9: 0,
            10: 0, 
            11: 1,
            12: 0,
            13: 1,
            14: 0,
            15: 0,
            16: 0,
            17: 1,
            18: 0,
            19: 1
        }
        counter = 0
        for num in range(left, right + 1):
            counter += prime_map[bin(num).count("1")]
        return counter