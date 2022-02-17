"""
=== Brute Force Approach ===
inner for-loop

~~Complexity Analysis
Time - O(n^2)

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, price in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if prices[j] <= price:
                    prices[i] = price - prices[j]
                    break
        return prices

=== Implemented Approach ===
I initially thought we might be able to solve in O(n) by going backwards
but realized that wouldn't work. Since my submission was pretty fast I figured
the brute force was the only way -- until I looked at the discussions. All I
saw was 

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, price in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if prices[j] <= price:
                    prices[i] = price - prices[j]
                    break
        return prices