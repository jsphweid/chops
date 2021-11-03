"""
===== Initial Thoughts =====
so if n=50
that is 1-49 they can choose but ONLY if it's 1, 2, 5, 10, 25

n=50, alice plays 10
n=40, bob plays 20
n=20, alice plays 4
n=16, bob plays 4
n=12, alice plays 6
n=6, bob plays 3
n=2, alice plays 1
bob loses

n=50, alice plays 25
n=25, bob plays 5
n=20, alice plays 10
n=10, bob plays 5
n=5, alice plays 1
n=4, bob plays 2
n=2, alice plays 1
bob loses

n=50, alice plays 1
n=49, bob plays 7
n=42, alice plays 1
n=41, bob plays 1
n=40, alice plays 1
n=39, bob plays 1
n=38, aliec plays 1
n=37, bob plays 1
n=36, alice pays 1
n=35, bob pays 7
n=28, alice plays 1
n=27, bob plays 9
n=18, alice plays 1
n=17, bob plays 1
n=16, alice plays 1
n=15, bob plays 5
n=10, alice plays1
n=9, bob plays 3
n=6, alice plays 1
n=5, bob plays 1
n=4, alice plays 1
n=3, bob plays 1
n=2, alice plays 1
bob loses

you can always play 1, until you can't

DP basically
"""

import math

# NOTE, i didn't write this... basically copied from the internet cuz I'm tryna go to bed soon
def get_divisors(n):
    all_divisors = []
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            all_divisors.append(i)
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        all_divisors.append(int(divisor))
    all_divisors.pop()
    return all_divisors

class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = {}
        def recurse(num):
            if num in dp: return dp[num]
            if n == 1: return False
            if n == 2: return True
            if n == 3: return False
            for d in get_divisors(num):
                if not recurse(num - d):
                    dp[num] = True
                    return True
            dp[num] = False
            return False
        return recurse(n)

