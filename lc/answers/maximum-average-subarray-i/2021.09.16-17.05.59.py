"""
A naive implementation could just sum up every item in the window and divide by k
over and over again. That'll do for a first pass.

So that solution didn't complete in time, almost went to happy hour but decided to finish it
using a more proper method.
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        running_sum = sum(nums[0: k])
        m = running_sum / k
        for i in range(k, len(nums)):
            running_sum += nums[i]
            running_sum -= nums[i - k]
            m = max(m, running_sum / k)
        return m