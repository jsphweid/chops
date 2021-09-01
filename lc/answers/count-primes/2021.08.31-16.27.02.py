"""
I can only imagine brute forcing this. We can check to see if a number
is prime by trial division.
100
1*100
2*50
4*25
5*20
10*10

36
1*36
2*18
3*12
4*9
6*6

We only care about it up to the sqrt. But we do care about the sqrt.

above 2, only odd numbers are prime
"""

def num_is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num < 4:
        return True
    highest = int(num ** 0.5) + 1
    possibilities = 0
    for i in range(1, highest + 1):
        if num % i == 0:
            possibilities += 1
        if possibilities > 1:
            return False
    return True


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        answers = {2: 0, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4}
        if n in answers:
            return answers[n]

        num_primes = 4
        for i in range(9, n, 2):
            if num_is_prime(i):
                num_primes += 1
        return num_primes


