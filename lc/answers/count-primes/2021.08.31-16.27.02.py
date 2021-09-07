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

count = 0
[3, 5, 7, 9]
count = 1
[5, 7]
count = 2
[7]
count = 3
[]
count = 4

aaron's
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 30]
count = 0
[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
count = 1
[5, 7, 11, 13, 17, 19, 23, 25, 29]
count = 2
[7, 11, 13, 17, 19, 23, 29]
count = 3

aaron's solution was elegant
```
class Solution:
    def countPrimes(self, n: int) -> int:
        r = list(range(2, n))
        count = 0
        while len(r):
            count += 1
            r = [i for i in r if i % r[0] != 0]
        return count
```

but still not fast enough

read some answers... we need to use `sieve of eratosthenes` like what aaron did but in a way that loops only over numbers
up to the ** 0.5. Also by using python list tools it should be super speedy. NOTE: I looked up a solution on this but am re-implementing it
without directly looking at it.

root = 4

2, 3

[0, 0, 1, 1, 1, 1, 1, 1, 1]

n=3
root =

[1, 1]

"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        lst = [1] * n
        lst[0] = 0
        lst[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if lst[i]:
                lst[i*i:n:i] = [0] * len(lst[i*i:n:i])
        return sum(lst)

