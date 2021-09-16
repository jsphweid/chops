"""
we can sort the array first which is O(n log n). Ideally we do it in O(n) though

```
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product = 1
        for num in nums[-3:]:
            product *= num
        return product
```

I'm dumb and I didn't consider the question carefully enough... Also their examples didn't communicate
the point of the problem.

`[-100,-98,-1,2,3,4]` should be `39200` not `24`

One idea would be to get two negative numbers and largest positive but also get 3 largest postives
and just use max to find the biggest.

We could sort, then get two smallest. If they are negative, then use those
"""

def multiply(nums: List[int]) -> int:
    product = 1
    for num in nums:
        product *= num
    return product

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(multiply(nums[:2] + nums[-1:]), multiply(nums[-3:]))