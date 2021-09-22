"""
I thought about how this could be implemented using DP but wasn't quite sure how it should all work out.

Actually, glancing at the solutions, there doesn't appear to be a DP answer -- not sure why it's classified that way.

It did mention something about a better 1 pass solution. I'm realizing that I probably overcomplicated my solution.


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        return max_profit