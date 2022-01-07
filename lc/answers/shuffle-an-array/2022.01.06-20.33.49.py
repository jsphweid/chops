"""
===== Initial Thoughts =====
3.141592653589793 - 3 * 10
1 2 3 5 8 13 21 34... 

my original solution... wasn't random enough tho

def gen_random():
    a, b = 1, 2
    while True:
        nxt = a + b
        a, b = b, nxt
        yield nxt

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.gen = gen_random()

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        copy = self.original[:]
        res = []
        while copy:
            num = 0 if len(copy) == 1 else next(self.gen) % len(copy) - 1
            res.append(copy.pop(num))
        return res

using random...

from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        copy = self.original[:]
        res = []
        while copy:
            num = randint(0, len(copy) - 1)
            res.append(copy.pop(num))
        return res


then using random()
from random import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        copy = []
        for item in self.original:
            copy.append((random(), item))
        copy.sort()
        return [item[1] for item in copy]
"""


from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        copy = self.original[:]
        for i in range(len(copy) - 1, -1, -1):
            r = randint(0, i)
            copy[i], copy[r] = copy[r], copy[i]
        return copy

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()