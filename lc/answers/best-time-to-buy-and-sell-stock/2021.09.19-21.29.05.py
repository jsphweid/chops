"""
brute force approach would simply be to iterate over the list and at each index, return the
max of the list that is remaining
[7,1,5,3,6,4]
max([1,5,3,6,4]) - 7 => -1
max([5,3,6,4]) - 1 => 5
max([3,6,4]) - 5 => 1
max([6,4]) - 3 => 3
max([4]) - 6 => -2

then do the max of all those results!

let's implement this...

made an error for first submission when I didn't think about the case where `max([])` can exist.
the second error was expected -- time limit exceeded. Why? Let's look at the time/space complexity

n == length of prices
- we iterate over n - 1 items
    - each iteration we 1.) slice (n-1)/2 prices (I think) 2.) then we max those, which is the same
- the we max profits, which is another n added

time: n^3 or n^3 - 2n^2 + n (polynomial?)
space: 2n (for profits, and any given iteration having worst case n-1 sell_prices)

```
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(0, len(prices) - 1):
            buy_price = prices[i]
            sell_prices = prices[i + 1:]
            profit = max(sell_prices) - buy_price
            profits.append(profit)
        return max(max(profits), 0) if len(profits) else 0
```

Getting back to this the next day...

The redundant computation seems to be comparing the same numbers to find the max

I think I figured out a non-DP way of doing this but it should be really efficient.

scan the list once backwards and max at each step, record the results in a dict which indicate the max at 
that index for the rest of the list
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = {}
        for i in range(len(prices) - 1):
            reverse_i = len(prices) - 1 - i
            prev = None if i == 0 else d[reverse_i + 1]
            d[reverse_i] = prev if (prev and prev > prices[reverse_i]) else prices[reverse_i]
        best = 0
        for i in range(len(prices) - 1):
            best = max(best, d[i + 1] - prices[i])
        return best

