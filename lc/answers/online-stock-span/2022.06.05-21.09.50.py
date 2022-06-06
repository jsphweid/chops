"""
   0  1  2  3  4  5  6
[100,80,60,70,60,75,85]
   1  1  1  2  1  4  6

[(0,100),(6,85)]


we're trying to find the previous next largest number.
so monotonic stack makes sense.
[(100,0),]

FAILED On [[],[31],[41],[48],[59],[79]]

Basically I didn't consider this case, where it always increases.
My if len(self.stack) == 1: return 1 is flawed
"""

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        while self.stack and price >= self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.day, price))
        if len(self.stack) == 1:
            return self.stack[0][0]
        return self.stack[-1][0] - self.stack[-2][0]
