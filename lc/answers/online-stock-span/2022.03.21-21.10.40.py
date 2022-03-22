"""
===== Initial Thoughts =====
[100,80,60,70,60,75,85]
feels like a stack problem
100 80 60 70 60 75
100,0  85,6
  85,6

return 2
return 4

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        res = self.idx - (self.stack[-1][1] if self.stack else -1)
        self.stack.append((price, self.idx))
        return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)