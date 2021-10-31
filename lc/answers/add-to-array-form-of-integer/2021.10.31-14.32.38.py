"""
===== Initial Thoughts =====
easy way out would be to convert num to an int... add them, then reconvert to a list.
"""

def list_to_num(lst):
    num = 0
    for i in range(len(lst)):
        power = len(lst) - 1 - i
        num += (lst[i] * (10 ** power))
    return num

# def list_to_num(lst):
#     return int("".join([str(n) for n in lst]))


# def num_to_list(num):
#     return [int(n) for n in list(str(num))]
import math
def num_to_list(num):
    if num == 0: return [0]
    num_digits = math.floor(math.log10(num)) + 1
    lst = []
    for i in range(num_digits):
        power = num_digits - 1 - i
        n = 10 ** power
        # how many n's can we take out?
        z = num // n
        lst.append(z)
        num -= (z * n)
    return lst

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return num_to_list(list_to_num(num) + k)