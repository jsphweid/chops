"""
Using divmod allows you to write an elegant solution.

  123  -> top
  456  -> bottom
x____
  738  -> results[0]
 6150  -> results[1]
49200  -> results[2]
+____
56088  -> sum(results)

Notice how `i` allows us to shift numbers around appropriately.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        results = []
        for i, char_bottom in enumerate(reversed(num2)):
            num, carry, bottom = 0, 0, int(char_bottom)
            for char_top in reversed(num1):
                top = int(char_top)
                carry, remainder = divmod(top * bottom + carry, 10)
                num += remainder * (10 ** i)
                i += 1
            num += carry * (10 ** i) if carry else 0
            results.append(num)
        return str(sum(results))
        