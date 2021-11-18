"""
=== Brute Force Approach ===
find every permutation of 1 -> n, and if it's a prime arrangement, increase count by 1
prime numbers up to 100 can be cached...

~~Complexity Analysis
Time - O(n!)
Space - O(1)

=== Implemented Approach ===
n = 1, res = 1
[1] -> True (because 1 is not prime, and index 1 is not prime)

n = 2, res = 1
[1,2] -> True
[2,1] -> False

n = 3, res = 2
[1,2,3] -> True
[1,3,2] -> True
[2,1,3] -> False
[2,3,1] -> False
[3,1,2] -> False
[3,2,1] -> False
3 numbers, 3*2*1 possibilities, each has 2, and there is 1 prime

n = 4, res = 4
[1,2,3,4]
[1,2,4,3] -> False
[1,3,2,4]
[1,3,4,2] -> False
[1,4,2,3] -> False
[1,4,3,2] -> False
[2,1,3,4] -> False
[2,1,4,3] -> False
[2,3,1,4] -> False
[2,3,4,1] -> False
[2,4,1,3] -> False
[2,4,3,1] -> False
[2,3,1,4] -> False
[2,3,4,1] -> False
[3,1,2,4] -> False
[3,1,4,2] -> False
[3,2,1,4] -> False
[3,2,4,1] -> False
[3,4,1,2] -> False
[3,4,2,1] -> False
[4,1,2,3] -> False
[4,1,3,2] -> False
[4,2,1,3] -> False
[4,2,3,1]
[4,3,1,2] -> False
[4,3,2,1]

4 numbers, 4*3*2*1 possibilities (24), each has 6, and there is 2 prime
in how many different ways can 4,1 be in those two positions
12=4

5 numbers, 5*4*3*2*1 possibilities (120), each has 24 possibilities, there are 3 primes
res=12

input=1  output=1  num_permutations=1   num_primes=0 output2=1/1    output3=100%
input=2  output=1  num_permutations=2   num_primes=1 output2=1/2    output3= 50%
input=3  output=2  num_permutations=6   num_primes=2 output2=2/6    output3= 33%
input=4  output=4  num_permutations=24  num_primes=2 output2=4/24   output3= 17%
input=5  output=12 num_permutations=120 num_primes=3 output2=12/120 output3= 10%

1/4 1/3 * 2 * 24 (num_permutations) => 4
4/24
2/12
1/6


1/5 1/4 * 2 * 120 (num_permutations) => 12

1/5 1/4 1/3 * 120

1/3 * 6 => 2 which makes sense

1/2 * 2 => 1 which makes sense

1/1 * 1 => 1 which makes sense

=================
input=5  output=12 num_permutations=120 num_primes=3 output2=12/120 output3= 10%
3/5 chance it'll be prime
2/5 chance it'll be non-prime

3/5 * 3/5 * 3/5 * 2/5 * 2/5 * 120 => NO
3/5 * 2/4 * 1/3 * 2/2 * 1/1 * 120=> 12 IT WORKS

input=4  output=4  num_permutations=24  num_primes=2 output2=4/24   output3= 17%
2/4 * 1/3


~~Complexity Analysis
Time - 
Space - 
"""

from fractions import Fraction

def get_num_primes_under_n(n: int):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    res = 0
    for prime in primes:
        if prime <= n: res += 1
        else: break
    return res

def get_num_permutations(n: int):
    res = 1
    for i in range(n):
        res *= (i + 1)
    return res

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        num_primes = get_num_primes_under_n(n)
        num_permutations = get_num_permutations(n)
        num = Fraction(1, 1)
        while num_primes > 0:
            num *= Fraction(num_primes, n)
            num_primes -= 1
            n -= 1
        res = int(num * num_permutations)
        return res % 1000000007
        