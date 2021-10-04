"""
===== Initial Thoughts =====
it's a windowing moving average... the order of the list matters... we have to go through all of them

=== Implemented Approach ===
k is window length -- slide it over through the numbers averaging them. if it beats some max, then rewrite the max

to do this efficiently, we need to NOT sum all the elements in the window every time.
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        last_sum = sum(nums[0: k])
        max_average = last_sum / k
        for i in range(k, len(nums)):
            num_to_add = nums[i]
            num_to_drop = nums[i - k]
            new_sum = last_sum + num_to_add - num_to_drop
            last_sum = new_sum
            new_average = new_sum / k
            max_average = max(max_average, new_average)
        return max_average
