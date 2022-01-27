"""
===== Initial Thoughts =====


=== Brute Force Approach ===
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        best = 0
        for x in nums:
            for y in nums:
                best = max(best, x ^ y)
        return best
                

~~Complexity Analysis
Time - O(n*n)
Space - O(1)

=== Implemented Approach ===
I think we have to answer... what makes an ^ high and how can we optimize that with a one-pass (most likely) solution.

Hmm, this is hard because numbers are fairly unpredictable with which 1s and 0s they have and where. Well, it's hard for me at least.

READING ANSWERS...

I thought about using a trie and that's literally the proposed solution. I still don't understand how it works 100% of the time.
A trie means go after the complement in a greedy way, only choose the wrong bit it you can't choose anything else. I feel like this
is a non-starter since there's inevitably going to be a better number where you choose the wrong one deliberately and it's a better fit.
for example given these three numbers:
10011
01111
11100

if we're looking for perfect compliment of 10011..., we'll start looking for a 0, this will mean we'll never persue number 3.
But number 3 is a better compliment than number 2. How do we justify this?

ACTUALLY, I just put those in the computer and turns out 2 IS better. The reason is because bit priority. All numbers are not equal.
The ones on the left are more important. i.e. 0111 is not as big as 1000. So that first bit really matters if you can help it since it's worth
more than all the others combined. THIS WAS WHAT I WAS MISSING. I was just going off of pure overlap of 1's and 0's. That's a grave mistake.

Now I can do this problem.


[3,10,5,25,2,8]
['00011', '01010', '00101', '11001', '00010', '01000']

trie
{
    '0': {
        '0': {
            '0': {
                '1': {
                    '1': {
                        '*': 3
                    }
                }
            }
        },
        '1': {
            etc.
        }
    }
}
"""

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # find max length
        bins = [bin(n)[2:] for n in nums]
        max_len = max([len(b) for b in bins])
        bins = [b if len(b) == max_len else ('0' * (max_len - len(b))) + b for b in bins]

        # put everything in a trie
        trie = {}
        for i, n in enumerate(nums):
            curr = trie
            for char in bins[i]:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr["*"] = n

        # run through numbers finding best matches
        best = 0
        for i, n in enumerate(nums):
            curr = trie
            for char in bins[i]:
                comp = '1' if char == '0' else '0'
                curr = curr[comp if comp in curr else char]
            best = max(best, curr["*"] ^ n)

        return best



