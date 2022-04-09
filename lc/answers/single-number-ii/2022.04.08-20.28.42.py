"""
===== Initial Thoughts =====
xor ^
and &
or |
bit shift << and >>
!4
compliment~

sum everything.
maybe xor everything to get a number
use that number to replace everything
get sum of that... subtract?

nope

[2,2,3,2] => 9
[2,3] => 5 (after removing duplicates)

READ SOME SOLUTIONS

they are all insane.
One kinda made sense...
just count the freq of each bit... keep all the ones that are not
divisible by 3. Those represent the bits of the final number
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        state = [0] * 32
        for num in nums:
            rep = bin(num)[2 + (num < 0):][::-1]
            for i in range(31, 31 - len(rep), -1):
                j = 32 - i - 1
                state[i] += int(rep[j])
        state = [s % 3 != 0 for s in state]
        state = [str(int(i)) for i in state]
        res = int("".join(state), 2)
        cnt = sum([n == res for n in nums])
        return res if cnt == 1 else -res
