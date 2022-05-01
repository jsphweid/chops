"""
failed on 
1 + 3
[4,5,2,4,3,3,1,2,5,4]
1

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)

        if N <= 1:
            return 0

        @cache
        def get_max(i):
            if i + 1 >= N:
                return 0
            buy = prices[i] + fee
            most_profit = 0
            for j in range(i + 1, N):
                profit = prices[j] - buy
                if profit > 0:
                    most_profit = max(most_profit, profit + get_max(j + 1))
            return most_profit

        return max([get_max(i) for i in range(N - 1)])

get_max(i=2)

This approach fundamentally doesn't work because for i=2, it's going to return one with
the most profit being buy at v=2 and sell at v=5. This is true, but the range covered by that
is too large. Really, we want the largest from index 2 to like index 6. since index 6 to end
is already covered.

Really we need to incorporate that start at every index philosophy into the fn.

[9,8,7,1,2]
3

Finally got a brute force

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        if N <= 1: return 0

        @cache
        def get_max_after(i):
            if i + 1 >= N:
                return 0
            best = 0
            for j in range(i, N - 1):  # buy day
                buy = prices[j] + fee
                for k in range(j + 1, N):  # sell day
                    profit = prices[k] - buy
                    if profit > 0:
                        best = max(best, profit + get_max_after(k + 1))
            return best
        return get_max_after(0)

even going backwards doesn't help

Read another recursive solution that I liked... let's try that.
I'll look at greedy shortly but I don't see myself magically getting an answer like
that in an interview situation. So I'll settle for recursion for now.

Another way recursion could be viewed (as opposed to above) is you have only 3 options
buy, sell, hold
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def find_max(i, can_buy):
            if i >= len(prices):
                return 0
            best = 0
            if can_buy:
                best = max(best, -prices[i] - fee + find_max(i + 1, False))
            else:
                best = max(best, prices[i] + find_max(i + 1, True))
            best = max(best, find_max(i + 1, can_buy))
            return best
        return find_max(0, True)

