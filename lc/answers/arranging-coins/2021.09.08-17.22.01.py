"""
brute force solution here is to just iterate up to the number
keeping a second counter

That doesn't work because it times out though...

```
class Solution:
    def arrangeCoins(self, n: int) -> int:
        current_level = 1
        level_counter = current_level
        for _ in range(n):
            if level_counter == 0:
                current_level += 1
                level_counter = current_level
            level_counter -= 1
        return current_level if level_counter == 0 else current_level - 1
```

I kinda looked at the answers for a few seconds and noticed the math path
exists as I suspected. But it's not a clear equation. The truest thing
we can say mathematically is that k * (k + 1) <= 2n. But my math skills aren't strong enough to get to a `k = ???`

We can get k**2 + k - 2n <= 0, but not sure how to get `k=`

Looking at answer more...

apparently we can use "Completing the square"

I practiced this technique and it works well, damn!
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(((0.25 + (2 * n)) ** 0.5) - 0.5)
