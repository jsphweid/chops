"""
we solved it using math (with a bit of help)

I noticed that the solutions also mentioned a nlogn approach using binary search.

How could we use that?
I get that it's all based off `n` and `k` but how do we test `k`
    - there has to be a way of knowing immediately, right? Although arguably if there were then finding k wouldn't be so
    hard that we'd need to apply any more than elementary math to (okay... so it's middle school math)

What is the maximum `k` to have as a goal post?

The algorithm listed in the 1st answer/approach is to still understand the dividing point between each k
k(k+1)//2
we use that as a test. But curiously we only decrease/increase the goal post by 1. I don't immediately understand why this
is since that doesn't seem to lead to logn time in the way other binary search algorithms I've written have done so.
Actually upon closer inspection the goal posts are converted from 0-n to jumping from k-k. Interesting.

I will probably shelve this for now as I'm burning out on it, but I'll keep in the mind the flexibility of binary search
for the future.


"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            k = (left + right) // 2
            result = (k * (k + 1)) // 2
            if result == n:
                return k
            elif result > n:
                right = k - 1
            else:
                 left = k + 1
        return right